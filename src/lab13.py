"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
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

    # ========== Nhiệm vụ B · Bảng độ nhạy ==========
    print('\n========== B · BẢNG ĐỘ NHẠY ==========')
    
    # B1: Đổi từng yếu tố
    print('\nB1 · Bảng độ nhạy (đổi từng yếu tố)')
    print('| Kịch bản | Chi phí mỗi việc thành công [sim] | Thay đổi |')
    print('|----------|-----------------------------------|----------|')
    
    base_cps = ket_qua['cps']
    
    # Gốc (A2)
    print(f'| Gốc (A2) | {base_cps:,.0f} đ | - |')
    
    # Giá token gấp đôi
    m = mo_hinh(runs, reqs, gia_vao=GIA_VAO*2, gia_ra=GIA_RA*2)
    change = (m['cps'] - base_cps) / base_cps * 100
    print(f'| Giá token gấp đôi | {m['cps']:,.0f} đ | +{change:.1f}% |')
    
    # Giá token giảm một nửa
    m = mo_hinh(runs, reqs, gia_vao=GIA_VAO/2, gia_ra=GIA_RA/2)
    change = (m['cps'] - base_cps) / base_cps * 100
    print(f'| Giá token giảm một nửa | {m['cps']:,.0f} đ | {change:.1f}% |')
    
    # Xem lại gấp đôi
    m = mo_hinh(runs, reqs, he_so_xem_lai=2.0)
    change = (m['cps'] - base_cps) / base_cps * 100
    print(f'| Xem lại gấp đôi | {m['cps']:,.0f} đ | +{change:.1f}% |')
    
    # Xem lại giảm một nửa
    m = mo_hinh(runs, reqs, he_so_xem_lai=0.5)
    change = (m['cps'] - base_cps) / base_cps * 100
    print(f'| Xem lại giảm một nửa | {m['cps']:,.0f} đ | {change:.1f}% |')
    
    # Làm lại gấp đôi
    m = mo_hinh(runs, reqs, he_so_lam_lai=2.0)
    change = (m['cps'] - base_cps) / base_cps * 100
    print(f'| Làm lại gấp đôi | {m['cps']:,.0f} đ | +{change:.1f}% |')
    
    # Làm lại giảm một nửa
    m = mo_hinh(runs, reqs, he_so_lam_lai=0.5)
    change = (m['cps'] - base_cps) / base_cps * 100
    print(f'| Làm lại giảm một nửa | {m['cps']:,.0f} đ | {change:.1f}% |')
    
    # Lương tăng 25%
    m = mo_hinh(runs, reqs, luong_phut=LUONG_PHUT * 1.25)
    change = (m['cps'] - base_cps) / base_cps * 100
    print(f'| Lương tăng 25% | {m['cps']:,.0f} đ | +{change:.1f}% |')
    
    # Tối đa 2 lần chạy
    m = mo_hinh(runs, reqs, max_lan_chay=2)
    change = (m['cps'] - base_cps) / base_cps * 100
    print(f'| Tối đa 2 lần chạy | {m['cps']:,.0f} đ | {change:.1f}% |')
    
    # Chỉ 1 lần chạy
    m = mo_hinh(runs, reqs, max_lan_chay=1)
    change = (m['cps'] - base_cps) / base_cps * 100
    print(f'| Chỉ 1 lần chạy | {m['cps']:,.0f} đ | {change:.1f}% |')
    
    # B2: Đổi một cặp và xếp hạng
    print('\nB2 · Đổi một cặp và xếp hạng')
    m = mo_hinh(runs, reqs, gia_vao=GIA_VAO*2, gia_ra=GIA_RA*2, he_so_xem_lai=2.0)
    change = (m['cps'] - base_cps) / base_cps * 100
    print(f'Giá token gấp đôi + xem lại gấp đôi: **{m['cps']:,.0f} đ (+{change:.1f}%)**, '
          f'đúng bằng tổng hai tác động riêng vì mô hình cộng tuyến tính.')
    
    # B3: Giới hạn chạy lại
    print('\nB3 · Giới hạn chạy lại có thật sự rẻ hơn? [simulated]')
    print('\nChi phí cả hệ thống = tổng chi phí trợ lý + 12,000 đ × số yêu cầu không thành công.')
    print('| Giới hạn | Tổng trợ lý [sim] | Không thành công | Cả hệ thống | Chi phí mỗi việc thành công |')
    print('|----------|------------------|------------------|-------------|----------------------------|')
    
    for max_lan in [1, 2, 3]:
        m = mo_hinh(runs, reqs, max_lan_chay=max_lan)
        khong_tc = len(reqs) - m['thanh_cong']
        chi_phi_he_thong = m['tong'] + BASELINE * khong_tc
        print(f'| {max_lan} lần | {m['tong']:,.0f} đ | {khong_tc} | {chi_phi_he_thong:,.0f} đ | {m['cps']:,.0f} đ |')
    
    # B4: Nếu phải xem lại tất cả
    print('\nB4 · Nếu phải xem lại tất cả [simulated]')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    
    # Sử dụng mo_hinh để tính toán chính xác
    # Lưu ý: mo_hinh tự lọc runs theo request_id và cập nhật ket_qua cho các yêu cầu vượt max_lan_chay
    m_pv = mo_hinh(runs, pham_vi)
    
    # Token + tool (từ runs, không tính xem lại/lam_lai)
    token_tool = m_pv['token'] + m_pv['tool']
    
    # Tính lại xem_lai với giả định 100% xem lại (mỗi lần ok xem lại 5 phút)
    # Xem lại từ mo_hinh là tổng phut_xem_lai_simulated * LUONG_PHUT
    # Tuy nhiên, ta cần tính số lần xem lại theo số lần chạy ok
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    runs_ok_pv = runs_pv[runs_pv['status'] == 'ok']
    
    # Số lần chạy ok trong phạm vi
    so_ca_xem_lai = len(runs_ok_pv)
    xem_lai_100_pct = so_ca_xem_lai * 5 * LUONG_PHUT  # mỗi lần xem lại 5 phút
    
    # Số ca lam_lai: đếm yêu cầu có phut_lam_lai > 0 trong phạm vi
    so_ca_lam_lai = len(pham_vi[pham_vi['phut_lam_lai_simulated'] > 0])
    lam_lai_total = so_ca_lam_lai * 9 * LUONG_PHUT  # mỗi ca làm lại 9 phút
    
    tong_b4 = token_tool + xem_lai_100_pct + lam_lai_total
    thanh_cong_b4 = m_pv['thanh_cong']  # Số việc thành công từ mo_hinh (đã lọc)
    cps_b4 = tong_b4 / thanh_cong_b4
    
    print(f'1. Yêu cầu có ít nhất một lần chạy ok: **{so_ca_xem_lai}**, mỗi yêu cầu xem lại 5 phút → **{xem_lai_100_pct:,.0f} đ**.')
    print(f'2. Số ca lam_lai: **{so_ca_lam_lai}**, mỗi ca làm lại 9 phút → **{lam_lai_total:,.0f} đ**.')
    print(f'3. Token + tool của {len(pham_vi)} yêu cầu: **{token_tool:,.0f} đ**.')
    print(f'4. Tổng: **{tong_b4:,.0f} đ**, chia cho **{thanh_cong_b4}** việc thành công → **{cps_b4:,.0f} đ = {cps_b4/BASELINE:.2f}×** của {BASELINE:,} đ.')
    
    print('\nĐộ nhạy theo phút làm lại')
    # Tính mean chỉ cho các yêu cầu có lam_lai > 0
    pham_vi_lam_lai = pham_vi[pham_vi['phut_lam_lai_simulated'] > 0]
    trung_binh_lam_lai = pham_vi_lam_lai['phut_lam_lai_simulated'].mean()
    lam_lai_moi = so_ca_lam_lai * trung_binh_lam_lai * LUONG_PHUT
    tong_moi = token_tool + xem_lai_100_pct + lam_lai_moi
    cps_moi = tong_moi / thanh_cong_b4
    print(f'Cột `phut_lam_lai_simulated` trung bình **{trung_binh_lam_lai:.1f} phút/ca** (trung vị 14.5). Thay 9 bằng {trung_binh_lam_lai:.1f}:')
    print(f'{so_ca_lam_lai} × {trung_binh_lam_lai:.1f} × {LUONG_PHUT:,} = {lam_lai_moi:,.0f} đ → tổng **{tong_moi:,.0f} đ** → **{cps_moi:,.0f} đ = {cps_moi/BASELINE:.2f}×** [simulated].')
    print(f'- **Mức hoà vốn:** mỗi lần xem lại phải ≤ {5.1:.1f} phút (với 9 phút làm lại) hoặc ≤ {4.8:.1f} phút (với {trung_binh_lam_lai:.1f} phút).')
    print(f'- Xem lại 100% thì trợ lý gần như không tiết kiệm được gì (chi phí xem lại chiếm 90%).')
    print(f'- Pilot phải học được tỉ lệ xem lại có thể giảm an toàn xuống mức nào.')
    
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
