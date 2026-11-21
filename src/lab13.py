"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import os
import re
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    # Tử số: MỌI lần chạy (kể cả lần lỗi). Nhớ chia 1.000 trước khi nhân giá token.
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    # Mẫu số: chỉ đếm yêu cầu thành công
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


# ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
LOAI = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']


def theo_loai(runs, reqs):
    """Bảng A3: mỗi loại một dòng (cps là simulated vì có xem lại + làm lại)."""
    dong = []
    for loai in LOAI:
        sub = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, sub)  # hàm đã tự lọc runs theo request_id
        dong.append(dict(loai=loai, so_yc=len(sub), ti_le_tc=m['thanh_cong'] / len(sub),
                         lan_chay_moi_yc=sub['so_lan_chay'].mean(), cps=m['cps'],
                         so_voi_nv=m['cps'] / BASELINE))
    return pd.DataFrame(dong)


def ti_le_ok_theo_lan(runs, reqs):
    """Tỉ lệ status == ok theo loại và theo lần thử: chạy lại có giúp không?"""
    r = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    r['ok'] = (r['status'] == 'ok').astype(float)
    return r.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')


# ---------- Nhiệm vụ A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ----------
CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng
YC_MOI_THANG = 45_000


def chi_phi_co_dinh(runs, reqs):
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    m = mo_hinh(runs, pham_vi)
    thanh_cong_ty_le = m['thanh_cong'] / len(reqs)      # 900/1.200: việc thành công trong phạm vi / mẫu
    dong = []
    for ten, he_so in [('45.000 yêu cầu/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        viec_thang = YC_MOI_THANG * he_so * thanh_cong_ty_le
        cd = CHI_PHI_CO_DINH / viec_thang
        dong.append(dict(khoi_luong=ten, viec_thang=viec_thang, co_dinh=cd,
                         cps_cong_co_dinh=m['cps'] + cd, so_voi_nv=(m['cps'] + cd) / BASELINE))
    return m['cps'], pd.DataFrame(dong)


def he_thong(runs, reqs):
    """Chi phí cả hệ thống mỗi yêu cầu = (tổng trợ lý + 12.000 × yêu cầu không thành công) / số yêu cầu."""
    m = mo_hinh(runs, reqs)
    khong_tc = len(reqs) - m['thanh_cong']
    return (m['tong'] + BASELINE * khong_tc) / len(reqs), khong_tc


# ---------- Nhiệm vụ B · Bảng độ nhạy ----------
# Mỗi kịch bản = một lần gọi mo_hinh với đúng một tham số đã đổi. Mọi kết quả B là simulated
# vì mô hình dùng phút xem lại / làm lại (cột *_simulated).
KICH_BAN = {
    'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),   # giá tool giữ nguyên
    'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
    'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
    'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
    'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
    'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
    'Lương tăng 25%':           dict(luong_phut=2500),
    'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
    'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
}


def do_nhay(runs, reqs):
    """B1: 9 kịch bản đổi từng yếu tố. Trả về (bảng, cps gốc)."""
    goc = mo_hinh(runs, reqs)['cps']
    dong = []
    for ten, kw in KICH_BAN.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        dong.append(dict(kich_ban=ten, cps=cps, thay_doi=(cps / goc - 1) * 100))
    return pd.DataFrame(dong), goc


def kiem_tra_mot_nua(bang):
    """Tự kiểm tra B1: mô hình tuyến tính nên mức giảm của 'giảm một nửa' = đúng nửa mức tăng của 'gấp đôi'."""
    d = bang.set_index('kich_ban')['thay_doi']
    for yeu_to in ('Giá token', 'Xem lại', 'Làm lại'):
        tang, giam = d[f'{yeu_to} gấp đôi'], d[f'{yeu_to} giảm một nửa']
        assert abs(giam + tang / 2) < 1e-6, f'{yeu_to}: giảm một nửa phải bằng nửa mức tăng gấp đôi'
    print('B1 · tự kiểm tra "giảm một nửa = nửa mức tăng gấp đôi": ĐẠT')


def xep_hang(bang):
    """Xếp hạng yếu tố theo mức tăng của kịch bản làm mạnh yếu tố đó lên (gấp đôi / lương +25%)."""
    muc_tang = {'số ca làm lại': bang.loc[bang.kich_ban == 'Làm lại gấp đôi', 'thay_doi'].iloc[0],
                'tỉ lệ xem lại': bang.loc[bang.kich_ban == 'Xem lại gấp đôi', 'thay_doi'].iloc[0],
                'lương nhân viên': bang.loc[bang.kich_ban == 'Lương tăng 25%', 'thay_doi'].iloc[0],
                'giá token': bang.loc[bang.kich_ban == 'Giá token gấp đôi', 'thay_doi'].iloc[0]}
    return sorted(muc_tang.items(), key=lambda kv: -kv[1])


def cap_doi(runs, reqs):
    """B2: đổi một cặp (giá token gấp đôi + xem lại gấp đôi) và so với tổng hai tác động riêng."""
    goc = mo_hinh(runs, reqs)['cps']
    cps = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    rieng = sum(mo_hinh(runs, reqs, **KICH_BAN[t])['cps'] / goc - 1
                for t in ('Giá token gấp đôi', 'Xem lại gấp đôi'))
    return cps, (cps / goc - 1) * 100, rieng * 100


def gioi_han_chay(runs, reqs):
    """B3: giới hạn 1/2/3 lần chạy. Cả hệ thống = tổng trợ lý + 12.000 × yêu cầu không thành công
    (nhân viên phải làm thay)."""
    dong = []
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - m['thanh_cong']
        dong.append(dict(gioi_han=k, tong_tro_ly=m['tong'], khong_thanh_cong=khong_tc,
                         ca_he_thong=m['tong'] + BASELINE * khong_tc, cps=m['cps']))
    return pd.DataFrame(dong)


def xem_lai_tat_ca(runs, reqs, phut_xem=5, phut_lam=9):
    """B4: bắt buộc xem lại 100% yêu cầu trong phạm vi noi_dia + hang_nang (simulated).
    - Xem lại: mọi yêu cầu có ít nhất một lần chạy status == ok, mỗi yêu cầu phut_xem phút.
    - Làm lại: các ca ket_qua == lam_lai, mỗi ca phut_lam phút.
    - Token + tool: MỌI lần chạy thuộc phạm vi. Mẫu số: số việc thành công trong phạm vi."""
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r = runs[runs['request_id'].isin(pv['request_id'])]
    n_xem = r.loc[r['status'] == 'ok', 'request_id'].nunique()
    n_lam = int((pv['ket_qua'] == 'lam_lai').sum())
    token_tool = ((r['tokens_in'] / 1000 * GIA_VAO + r['tokens_out'] / 1000 * GIA_RA).sum()
                  + (r['tool_calls'] * GIA_TOOL).sum())
    tien_xem, tien_lam = n_xem * phut_xem * LUONG_PHUT, n_lam * phut_lam * LUONG_PHUT
    tong = token_tool + tien_xem + tien_lam
    thanh_cong = int((pv['ket_qua'] == 'thanh_cong').sum())
    # phút xem lại tối đa để cps <= 12.000 đ (mức hoà vốn)
    hoa_von = (BASELINE * thanh_cong - token_tool - tien_lam) / (n_xem * LUONG_PHUT)
    return dict(so_yc=len(pv), n_xem=n_xem, n_lam=n_lam, phut_lam=phut_lam, token_tool=token_tool,
                tien_xem=tien_xem, tien_lam=tien_lam, tong=tong, thanh_cong=thanh_cong,
                cps=tong / thanh_cong, so_voi_nv=tong / thanh_cong / BASELINE, hoa_von_phut_xem=hoa_von)


# ---------- Nhiệm vụ D · Cỡ mẫu của pilot (D1) ----------
# Cho sẵn: baseline 0,70; mục tiêu +5 điểm; alpha 0,05; power 0,8; ICC 0,02.
BASELINE_CHINH = 0.70
ICC = 0.02
DUONG_DAN_PILOT_PLAN = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', 'report', 'team', 'pilot_plan.yaml')


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (chia theo yêu cầu, chưa tính hiệu ứng cụm)."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    """DE = 1 + (m - 1) × ICC, m = số yêu cầu mỗi cụm (mỗi nhân viên hoặc mỗi depot)."""
    return 1 + (m - 1) * icc


def so_yc_moi_cum_toi_thieu(n_can, so_cum, icc=ICC):
    """Giải  so_cum × m / (1 + (m - 1) × icc) >= n_can  → m >= n_can (1 - icc) / (so_cum - n_can × icc).
    Chỉ có nghiệm khi n_can < so_cum / icc (cỡ mẫu hiệu dụng luôn nhỏ hơn c / ICC)."""
    if n_can >= so_cum / icc:
        return None
    return math.ceil(n_can * (1 - icc) / (so_cum - n_can * icc))


def power_muc_5_diem(n_moi_nhom):
    """Power thực sự nếu tác động thật chỉ là 5 điểm (0,70 → 0,75) trong khi cỡ mẫu tính cho 6 điểm."""
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower
    h = proportion_effectsize(BASELINE_CHINH + 0.05, BASELINE_CHINH)
    return NormalIndPower().power(effect_size=h, nobs1=n_moi_nhom, alpha=0.05, ratio=1.0)


def cau_d1():
    """Năm câu D1. Mọi số trong pilot_plan.yaml lấy từ đây."""
    a = co_mau(BASELINE_CHINH, BASELINE_CHINH + 0.05)
    m_b = 75
    de_b = he_so_thiet_ke(m_b)
    n_b = math.ceil(a * de_b)
    n6 = co_mau(BASELINE_CHINH, BASELINE_CHINH + 0.06)      # mức chênh 6 điểm
    m_e = so_yc_moi_cum_toi_thieu(n6, 20)
    return dict(
        a_theo_yc=a,
        b_de=de_b, b_n=n_b, b_nguoi_moi_nhom=math.ceil(n_b / m_b), b_tong_nguoi=2 * math.ceil(n_b / m_b),
        c_toi_da=20 / ICC, c_dat=20 / ICC >= a,
        d_toi_da=6 / ICC, d_dat=6 / ICC >= a,
        e_n6=n6, e_m=m_e, e_de=he_so_thiet_ke(m_e), e_power_5_diem=power_muc_5_diem(n6))


def ti_le_mo_lai_hien_tai(reqs):
    """Tính TRƯỚC khi đặt ngưỡng an toàn: đợt chạy thử đang ở mức nào."""
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    return dict(toan_mau=reqs['mo_lai_trong_7_ngay'].mean(), pham_vi=pv['mo_lai_trong_7_ngay'].mean(),
                chuyen_nv_pham_vi=(pv['ket_qua'] == 'chuyen_nhan_vien').mean(),
                lam_lai_pham_vi=(pv['ket_qua'] == 'lam_lai').mean())


def kiem_tra_pilot_plan(duong_dan=DUONG_DAN_PILOT_PLAN):
    """Kiểm tra trước deadline: yaml.safe_load, không còn dấu hỏi, >= 3 luật dừng đủ bốn vế,
    đủ trường, số trong file khớp D1, không dùng từ cấm. Trả về danh sách lỗi (rỗng nghĩa là đạt)."""
    import yaml
    loi = []
    with open(duong_dan, encoding='utf-8') as f:
        text = f.read()
    plan = yaml.safe_load(text)['pilot']
    if any('?' in dong for dong in text.splitlines() if not dong.lstrip().startswith('#')):
        loi.append('còn dấu hỏi ngoài dòng chú thích')
    for tu in ('production', 'cả đội'):
        if tu in text.lower():
            loi.append(f'có từ cấm: {tu}')
    for truong in ('owner', 'scope', 'assignment', 'rollout', 'primary_metric', 'identifiability',
                   'stop_rules', 'interim_looks', 'rollback', 'decision_date', 'simulated_inputs'):
        if truong not in plan:
            loi.append(f'thiếu trường {truong}')
    mau_luat = re.compile(r'NẾU .+ TRONG .+ THÌ .+ KHÔNG THÌ .+')
    luat_dung = [r for r in plan.get('stop_rules', []) if mau_luat.fullmatch(r)]
    if len(luat_dung) < 3:
        loi.append(f'chỉ có {len(luat_dung)} luật dừng đủ bốn vế NẾU - TRONG - THÌ - KHÔNG THÌ (cần >= 3)')
    d1 = cau_d1()
    pm = plan.get('primary_metric', {})
    if pm.get('n_per_arm') != d1['e_n6']:
        loi.append(f"n_per_arm {pm.get('n_per_arm')} khác D1 ({d1['e_n6']})")
    if abs(pm.get('design_effect', 0) - round(d1['e_de'], 2)) > 0.01:
        loi.append(f"design_effect {pm.get('design_effect')} khác D1 ({d1['e_de']:.2f})")
    if pm.get('clusters_per_arm') != 20:
        loi.append('clusters_per_arm phải là 20')
    return loi


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print(f"\nA2 · hoá đơn token+tool / số yêu cầu = {ket_qua['hoa_don_moi_yc']:,.1f} đ (đo từ trace)")
    print(f"A2 · chi phí mỗi việc thành công = {ket_qua['cps']:,.0f} đ [simulated], "
          f"gấp {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần hoá đơn")
    for ten in ('token', 'tool', 'xem_lai', 'lam_lai'):
        print(f"   {ten:8s} {ket_qua[ten] / ket_qua['tong'] * 100:5.1f}% tổng chi phí")
    print(f"   giờ nhân viên (xem lại + làm lại) = "
          f"{(ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong'] * 100:.1f}% [simulated]")

    print('\nA3 · tách theo loại [simulated]')
    print(theo_loai(runs, reqs).to_string(index=False, float_format=lambda x: f'{x:,.3f}'))
    print('\nA3 · tỉ lệ ok theo lần thử (chạy lại có giúp không?)')
    print(ti_le_ok_theo_lan(runs, reqs).round(3).to_string())

    cps_pv, a4 = chi_phi_co_dinh(runs, reqs)
    print(f'\nA4 · chi phí mỗi việc thành công trong phạm vi noi_dia + hang_nang = {cps_pv:,.0f} đ [simulated]')
    print(a4.to_string(index=False, float_format=lambda x: f'{x:,.2f}'))
    hs, khong_tc = he_thong(runs, reqs)
    print(f'A2 · chi phí cả hệ thống mỗi yêu cầu = {hs:,.0f} đ = {hs / BASELINE:.2f}x của {BASELINE:,} đ '
          f'[simulated] ({khong_tc} yêu cầu nhân viên làm thay)')

    # ---- Nhiệm vụ B (CP2) ----
    bang_b1, goc = do_nhay(runs, reqs)
    print(f'\nB1 · độ nhạy, gốc = {goc:,.0f} đ [simulated]')
    for _, d in bang_b1.iterrows():
        print(f'   {d.kich_ban:25s} {d.cps:8,.0f} đ {d.thay_doi:+6.1f}%')
    kiem_tra_mot_nua(bang_b1)

    cps_cap, thay_cap, tong_rieng = cap_doi(runs, reqs)
    print(f'B2 · token gấp đôi + xem lại gấp đôi = {cps_cap:,.0f} đ ({thay_cap:+.1f}%), '
          f'tổng hai tác động riêng = {tong_rieng:+.1f}% [simulated]')
    print('B2 · xếp hạng: ' + ' · '.join(f'{i}. {ten} ({muc:+.1f}%)'
                                         for i, (ten, muc) in enumerate(xep_hang(bang_b1), 1)))

    b3 = gioi_han_chay(runs, reqs)
    print('\nB3 · giới hạn chạy lại [simulated]')
    print(b3.to_string(index=False, float_format=lambda x: f'{x:,.0f}'))
    re_nhat = b3.loc[b3.ca_he_thong.idxmin(), 'gioi_han']
    cps_thap = b3.loc[b3.cps.idxmin(), 'gioi_han']
    them = (b3.loc[b3.gioi_han == cps_thap, 'khong_thanh_cong'].iloc[0]
            - b3.loc[b3.gioi_han == re_nhat, 'khong_thanh_cong'].iloc[0])
    print(f'B3 · rẻ nhất cho công ty: {re_nhat} lần; cps thấp nhất: {cps_thap} lần; '
          f'chọn theo cps thì đẩy thêm {them} việc sang nhân viên so với giới hạn {re_nhat} lần')

    phut_lam_tb = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    phut_lam_tv = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].median()
    print(f'\nB4 · xem lại 100% (noi_dia + hang_nang) [simulated]; '
          f'phút làm lại thật trung bình {phut_lam_tb:.1f} (trung vị {phut_lam_tv:.1f})')
    for nhan, phut in (('đề cho 9 phút/ca', 9), ('theo dữ liệu 15,3 phút/ca', 15.3)):
        b4 = xem_lai_tat_ca(runs, reqs, phut_lam=phut)
        print(f"   {nhan:26s}: xem lại {b4['n_xem']} × 5 phút = {b4['tien_xem']:,.0f} đ; "
              f"làm lại {b4['n_lam']} ca = {b4['tien_lam']:,.0f} đ; token+tool {b4['token_tool']:,.0f} đ; "
              f"tổng {b4['tong']:,.0f} đ / {b4['thanh_cong']} = {b4['cps']:,.0f} đ = {b4['so_voi_nv']:.2f}x; "
              f"hoà vốn: xem lại ≤ {b4['hoa_von_phut_xem']:.1f} phút")

    # ---- Nhiệm vụ D (CP4) ----
    d1 = cau_d1()
    print('\nD1 · cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02)')
    print(f"   a · chia theo yêu cầu: co_mau(0.70, 0.75) = {d1['a_theo_yc']:,} yêu cầu mỗi nhóm")
    print(f"   b · theo nhân viên, m = 75: DE = {d1['b_de']:.2f}; n = {d1['b_n']:,} mỗi nhóm "
          f"→ {d1['b_nguoi_moi_nhom']} người mỗi nhóm, tổng {d1['b_tong_nguoi']} > 40: không đủ người")
    print(f"   c · 20 nhân viên mỗi nhóm: tối đa 20 / 0,02 = {d1['c_toi_da']:,.0f} < {d1['a_theo_yc']:,}: "
          f"{'đạt' if d1['c_dat'] else 'không đạt'}")
    print(f"   d · 6 depot mỗi nhóm: tối đa 6 / 0,02 = {d1['d_toi_da']:,.0f} (không đạt {d1['a_theo_yc']:,})")
    print(f"   e · mức chênh 6 điểm ({d1['e_n6']} mỗi nhóm), 20 người mỗi nhóm: "
          f"m >= {d1['e_m']} yêu cầu mỗi người (DE {d1['e_de']:.2f})")
    print(f"   power thực sự nếu tác động chỉ là 5 điểm, n = {d1['e_n6']}: {d1['e_power_5_diem']:.2f}")
    mo_lai = ti_le_mo_lai_hien_tai(reqs)
    print(f"D3 · tỉ lệ mở lại 7 ngày hiện tại: toàn mẫu {mo_lai['toan_mau'] * 100:.2f}%, "
          f"phạm vi noi_dia + hang_nang {mo_lai['pham_vi'] * 100:.2f}% "
          f"(chuyển nhân viên {mo_lai['chuyen_nv_pham_vi'] * 100:.2f}%, làm lại {mo_lai['lam_lai_pham_vi'] * 100:.2f}%)")
    if os.path.exists(DUONG_DAN_PILOT_PLAN):
        loi = kiem_tra_pilot_plan()
        print('pilot_plan.yaml: ĐẠT' if not loi else 'pilot_plan.yaml: CÓ LỖI → ' + '; '.join(loi))
