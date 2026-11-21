# Báo cáo nhóm

Mọi số tính từ cột `_simulated` ghi nhãn [simulated].

## 1. Thông tin nhóm

- Tên nhóm: DLB
- Lớp: L3A
- Repo: `K5-L3A-DAY13-DLB-LaunchEconomics`
- Thành viên: Nguyễn Vũ Thành Long (2A202603635), Nguyễn Quang Đạo (2A202603614), Nguyễn Gia Bảo (2A202603647); chi tiết vai trò trong `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a duyệt kế hoạch pilot, trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định.

Cách tiếp cận:

- Mọi số do `src/lab13.py` tính, hoặc tính tay có ghi cách tính; đối chiếu với số trong hướng dẫn sau mỗi checkpoint.
- Nhóm 3 người nên gộp bốn vai của đề: người viết code đổi sau giờ giải lao (CP1 Long, CP2 Đạo, CP2 hoàn thiện và CP4 Long); người giữ hồ sơ kiêm người gắn nhãn 2 (Bảo).
- Mỗi thay đổi lớn đi qua nhánh riêng và pull request, có review trước khi merge vào `main`.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Chi phí mỗi việc thành công | Ba hàm A1 và `mo_hinh()`: tử số cộng token, tool của mọi lần chạy kể cả lỗi, cộng phút xem lại và làm lại; mẫu số chỉ đếm `thanh_cong`. Tách theo loại (A3), cộng chi phí cố định cho phạm vi noi_dia + hang_nang (A4) | `src/lab13.py`, [bang_chi_phi.md](bang_chi_phi.md) |
| B · Độ nhạy | Gọi lại `mo_hinh()` cho 9 kịch bản (B1), một cặp (B2), giới hạn 1/2/3 lần chạy với chi phí cả hệ thống (B3), xem lại 100% (B4) | `src/lab13.py`, [bang_chi_phi.md](bang_chi_phi.md) |
| C · Bảng lỗi | Hai người gắn nhãn độc lập 20 ca theo năm loại PAIR, so nhãn, thống nhất ca lệch; bảng khắc phục 5 ca, mỗi loại một ca | [bang_loi.md](bang_loi.md) |
| D · Pilot plan | Tính năm câu D1 trước rồi mới chọn cách chia; năm câu D2; tính tỉ lệ mở lại hiện tại trước khi đặt luật an toàn | `src/lab13.py`, [pilot_plan.yaml](pilot_plan.yaml) |
| E · Chỉ số, event, rủi ro, hồ sơ | Tính thử ba chỉ số (`chi_so_e1`), 11 event có `trace_id`, 4 dòng rủi ro lấy số từ bảng độ nhạy; ghép thành hồ sơ một trang bảy mục | [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md) |

## 4. Kết quả

- **A:** ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25). Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3× [simulated] hoá đơn token + tool chia số yêu cầu (274,7 đ). Chi phí cả hệ thống 5.865 đ/yêu cầu [simulated] = 0,49× [simulated] của 12.000 đ. quoc_te 1,88× [simulated] và doi_tac 0,85× [simulated] bị loại khỏi phạm vi.
- **B:** xếp hạng 1. số ca làm lại (+51,8% [simulated]) · 2. tỉ lệ xem lại (+40,7% [simulated]) · 3. lương (+23,1% [simulated]). Giới hạn 2 lần chạy rẻ nhất cho công ty. Xem lại 100%: 11.743 đ [simulated] = 0,98× [simulated], 12.415 đ [simulated] = 1,03× [simulated] nếu làm lại 15,3 phút/ca [simulated].
- **C:** đồng thuận 19/20 = 95%; ca 13 thống nhất Giới hạn hệ thống.
- **D:** chọn chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm: mỗi nhánh 5.980 yêu cầu thực tế, cỡ mẫu hiệu dụng ≈ 859 (DE 6,96); power 0,64 nếu tác động thật là 5 điểm. 5 luật dừng; đọc kết quả 2027-02-11. Đủ năm câu D1 trong `pilot_plan.yaml`.
- **E:** chỉ số trong đợt chạy thử: chính 82,83%, dùng 27,12%, an toàn 4,25% (chưa có đối chứng nên chưa kết luận tác động).
- **Đề xuất:** Go có điều kiện cho pilot noi_dia + hang_nang, kèm các con số bất lợi và 5 điều kiện có vai trò phụ trách, ngày kiểm tra.
- **Duyệt chéo Gate 2a:** nhóm hội đồng: ... · điểm: ... / 30 · quyết định: ... · câu hỏi và câu trả lời: ... (điền sau buổi duyệt chéo).

## 5. Khó khăn và cách xử lý

| Khó khăn | Bằng chứng | Cách xử lý |
| --- | --- | --- |
| `python lab13.py` lỗi khi in tiếng Việt trên Windows | `UnicodeEncodeError: 'charmap' codec can't encode character` (console cp1252) | Chạy với `$env:PYTHONIOENCODING = "utf-8"` |
| Một máy thiếu thư viện, code dừng ở D1 | `ModuleNotFoundError: No module named 'statsmodels'` | Tạo `src/.venv`, `pip install -r requirements.txt`; chạy lại hết, in `pilot_plan.yaml: ĐẠT` |
| Hai người cùng sửa `ho_so_launch_v0.md` trong cùng khoảng thời gian, bản nháp có số dễ bị trừ điểm (0,37× [simulated], "cao hơn baseline 0,70", trạng thái ngoài ba giá trị cho phép) | Commit `5fe928c`, PR #3 | Gộp hai bản về mẫu bảy mục, lấy số đã đối chiếu, review trước khi merge (PR #3) |
| Bản nháp đầu của `bang_loi.md` điền sẵn bộ nhãn 2 trước khi người gắn nhãn 2 gắn, ghi đồng thuận 100% | Commit `5fe928c`, PR #4 | Người gắn nhãn 2 gắn độc lập 20 ca; người gắn nhãn 1 xác nhận bộ nhãn 1 là tự gắn độc lập; ghi đồng thuận thật 19/20 (PR #4) |
| B4 lệch giữa code và hồ sơ: 16,25 phút/ca [simulated] (48 ca trong phạm vi) so với 15,3 phút/ca [simulated] (74 ca toàn mẫu) | Commit `d3206b5`, `f531cc7` | Từ `f531cc7`, code dùng 15,3 phút/ca [simulated], khớp kịch bản trong hồ sơ |

## 6. Tổng hợp đóng góp

| Thành viên | Vai | Đóng góp chính | Bằng chứng |
| --- | --- | --- | --- |
| Nguyễn Vũ Thành Long | Người viết code (CP1, CP4), hoàn thiện code CP2 | A1–A4 trong `lab13.py`; hoàn thiện B1–B4 và thống nhất B4; D1 và hàm kiểm tra `pilot_plan.yaml` trong code; hoàn thiện `pilot_plan.yaml` (D1, D2, 5 luật dừng) | Commit `71e2be4`, `31bd49c`, `f531cc7`, `49ff94f`; `2A202603635_NguyenVuThanhLong.md` |
| Nguyễn Quang Đạo | Người viết code CP2, người gắn nhãn 1, kiểm số CP1 | Code B1–B4 bản đầu; bản nháp đầu các file hồ sơ; bộ nhãn 1 (20 ca độc lập) | Commit `5fe928c`, `d3206b5`; `TEAM.md` (kiểm số CP1); `2A202603614_NguyenQuangDao.md` |
| Nguyễn Gia Bảo | Người gắn nhãn 2 kiêm giữ hồ sơ, kiểm số | Hồ sơ launch v0 bảy mục; bộ nhãn 2 và bảng lỗi; `chi_so.md`, E1 trong `lab13.py` | PR #3, #4, #8; `2A202603647_NguyenGiaBao.md` (PR #6) |

Chi tiết vai trò và đóng góp xem `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; pilot phải thay bằng phút đo thật sau tuần 1 (điều kiện trong hồ sơ).
- Với 40 nhân viên, pilot chỉ đủ mẫu cho mức chênh 6 điểm; nếu tác động thật là 5 điểm thì power chỉ 0,64.
- ICC 0,02 là giả định của lab; có thể kiểm bằng độ chênh tỉ lệ thành công giữa các `staff_id` trong dữ liệu mẫu.
- Bảng khắc phục dựa trên bảng mẫu của hướng dẫn, nhóm chỉ bổ sung mẫu số và tần suất cho ca 4, 7, 18.
- Lần sau: thống nhất mẫu file và người sửa từng file ngay đầu buổi, để tránh hai người sửa cùng một file và tránh lệch số giữa code với hồ sơ.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com.
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`).
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và `docs/du_lieu_va_cong_thuc.md` (số đối chiếu, công thức, bảng khắc phục mẫu).
