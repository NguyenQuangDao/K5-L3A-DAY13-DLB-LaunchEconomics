# Báo cáo cá nhân — Nguyễn Vũ Thành Long - 2A202603635

## 1. Thông tin thành viên

- Họ tên: Nguyễn Vũ Thành Long
- MSSV: 2A202603635
- Email: 26ai.longnvt2@vinuni.edu.vn
- Vai trong nhóm: người viết code (CP1; CP2 phần code B1-B4 trong `src/lab13.py`), người kiểm số (CP2), phụ trách `pilot_plan.yaml` và code D1 (CP4). Nhóm có 3 người nên không có vai người gắn nhãn 2 riêng; vai đó gộp vào Bảo cùng việc giữ hồ sơ.

## 2. Phần việc phụ trách

- **CP1 · Nhiệm vụ A:** ba hàm A1, `mo_hinh()`, tách theo loại yêu cầu (A3), chi phí cố định (A4).
- **CP2 · Nhiệm vụ B:** code bảng độ nhạy B1-B4 trong `src/lab13.py` và bảng B1-B4 trong `report/team/bang_chi_phi.md`.
- **CP4 · Nhiệm vụ D:** code cỡ mẫu D1, năm câu D2, `report/team/pilot_plan.yaml`.
- CP3 (bảng lỗi) và CP5 (hồ sơ) không thuộc phần việc chính của mình; chỉ hỗ trợ đối chiếu số khi cần.

## 3. Đóng góp cụ thể

**CP1 (A)**
- Viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử 1,20 · 1,25 · 1,25 đều ĐẠT.
- Viết `mo_hinh()`: tử số cộng mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm yêu cầu `thanh_cong`. Kết quả: tổng chi phí 4.373.585 đ, 978 việc thành công, chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ).
- A3 (4 loại), A4 (cộng chi phí cố định 40 triệu đ/tháng: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× ở một nửa khối lượng [simulated]), và chi phí cả hệ thống 5.865 đ = 0,49× [simulated] để so với 12.000 đ.

**CP2 (B)**
- Viết `do_nhay`, `kiem_tra_mot_nua`, `xep_hang`, `cap_doi`, `gioi_han_chay`, `xem_lai_tat_ca` trong `src/lab13.py`, nên mọi số B do code tính ra.
- B1 đủ 9 kịch bản; xếp hạng làm lại (+51,8%) > xem lại (+40,7%) > lương (+23,1%); B2 token gấp đôi cùng xem lại gấp đôi là 6.543 đ (+46,3%).
- B3: giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ), giới hạn 1 lần có chi phí mỗi việc thấp nhất (4.111 đ), chọn theo chi phí mỗi việc thì đẩy thêm 85 việc sang nhân viên [simulated].
- B4: xem lại 100% là 11.743 đ = 0,98×; nếu làm lại 15,3 phút thì 12.415 đ = 1,03×; mức hoà vốn ≤ 5,1 và ≤ 4,8 phút xem lại [simulated].

**CP4 (D)**
- Viết `co_mau`, `he_so_thiet_ke`, `so_yc_moi_cum_toi_thieu`, `cau_d1`, `power_muc_5_diem`, `ti_le_mo_lai_hien_tai`. Năm câu D1: 1.251 · 3.103 (84 người, không đủ) · 1.000 · 300 · m ≥ 299 (DE 6,96); power 0,64 nếu tác động thật là 5 điểm.
- Viết `kiem_tra_pilot_plan()`, tự kiểm tra yaml mỗi lần chạy `lab13.py`: đọc được bằng `yaml.safe_load`, không còn dấu hỏi, có ít nhất ba luật dừng đủ bốn vế, số khớp D1.
- Viết lại `pilot_plan.yaml`: chú thích D1 a-e, D2 năm câu, đánh đổi đã chấp nhận, tỉ lệ mở lại hiện tại (4,25% toàn mẫu, 3,97% trong phạm vi); năm luật dừng đủ bốn vế, đặt ngưỡng sau khi xem số của đợt chạy thử (chuyển nhân viên 3,46%, làm lại 4,89%); lịch pilot khớp với `ho_so_launch_v0.md`.

**Xử lý sự cố khi làm chung**
- Khôi phục bảng A1 và A4 trong `bang_chi_phi.md` sau khi bản của một thành viên khác ghi đè (mất hai lần).
- Gộp code B1-B4: giữ bản tương thích Python 3.10 trở lên, vì bản kia dùng dấu nháy lồng nhau trong chuỗi f chỉ chạy được từ Python 3.12 trong khi đề yêu cầu từ 3.10.

## 4. Bằng chứng

- Commit: `71e2be4` và `31bd49c` (CP1), `f531cc7` (CP2), `49ff94f` (CP4); tác giả nvl191.
- File: `src/lab13.py` (chạy `cd src && python lab13.py`, in ba phép thử ĐẠT, bảng A, B, D1 và `pilot_plan.yaml: ĐẠT`), `report/team/bang_chi_phi.md` (A1-A4, B1-B4), `report/team/pilot_plan.yaml`.
- Con số chính: 4.472 đ [simulated] mỗi việc thành công; 16,3×; 51,8% làm lại; 6.901.220 đ (giới hạn 2 lần); 11.743 đ (xem lại 100%); 1.251 · 3.103 · 1.000 · 300 · 299; power 0,64.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Anthropic, mô hình Claude Sonnet 5.5) trong VS Code.
- **Dùng vào việc:** viết và chỉnh code trong `src/lab13.py`, điền các bảng trong `bang_chi_phi.md` và `pilot_plan.yaml`, rà lỗi, phát hiện và xử lý xung đột khi gộp code, giải thích khái niệm (vì sao tử số tính mọi lần chạy, cỡ mẫu hiệu dụng khi chia theo cụm).
- **Cách tự kiểm tra kết quả:**
  - Mình tự tính lại các con số chính để kiểm tra với kết quả của code, rồi đối chiếu với số mẫu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%; B4 làm lại 15,3 phút ra 12.415 đ, đề ghi 12.414, chênh do làm tròn).
  - Ba phép thử A1 phải ĐẠT trước khi làm tiếp; `kiem_tra_mot_nua` in ĐẠT; `kiem_tra_pilot_plan` in ĐẠT mỗi lần chạy.
  - Tính lại các số bằng một đoạn script riêng chỉ dùng thư viện `csv` chuẩn (không dùng pandas, không gọi `mo_hinh`), kết quả khớp với bảng. Script này không đưa vào repo.
  - Mọi con số trong hồ sơ do `lab13.py` tính ra; không dùng AI để bịa số hay nhãn.

## 6. Tự đánh giá

- **Kết quả:** mình hoàn thành ba checkpoint phụ trách (CP1, phần code của CP2 và CP4). `src/lab13.py` chạy từ đầu đến cuối, ba phép thử A1 ĐẠT, các bảng A1-A4, B1-B4, D1 khớp số đối chiếu trong sai số 2%, và `pilot_plan.yaml` qua kiểm tra tự động (đọc được bằng `yaml.safe_load`, không còn dấu hỏi, năm luật dừng đủ bốn vế).
- **Điều học được:**
  - Chi phí thật của trợ lý (4.472 đ mỗi việc thành công, gấp 16,3 lần hoá đơn token) chủ yếu là giờ nhân viên xem lại và làm lại (92,5% [simulated]), nên pilot phải theo dõi tỉ lệ làm lại và xem lại hơn là giá token.
  - Tối ưu riêng chi phí mỗi việc thành công (giới hạn 1 lần) không có lợi cho công ty bằng giới hạn 2 lần, vì đẩy thêm 85 việc sang nhân viên.
  - Khi chia pilot theo cụm, số cụm mới quyết định cỡ mẫu hiệu dụng: 20 nhân viên mỗi nhóm tối đa 1.000 < 1.251, nên phải chấp nhận mức chênh 6 điểm và nói rõ power chỉ còn 0,64 nếu tác động thật là 5 điểm.
  - Ngưỡng dừng phải đặt sau khi xem số của đợt chạy thử: ngưỡng mở lại tuyệt đối 3% sẽ dừng pilot ngay tuần đầu vì mức hiện tại đã là 4,25%.
- **Khó khăn gặp phải:** hai người cùng sửa `bang_chi_phi.md` và phần B1-B4 trong `lab13.py` nên bảng A1 và A4 bị ghi đè hai lần, còn bản code B của một thành viên khác không chạy được trên Python 3.10 và 3.11. Mình đã khôi phục bảng và giữ bản code tương thích. Bản `pilot_plan.yaml` ban đầu cũng cần sửa vài chỗ: ngưỡng chuyển nhân viên 20% quá lỏng so với mức hiện tại 3,46%, định nghĩa hai chỉ số chia sai mẫu số, lịch pilot lệch với hồ sơ.
- **Bài học và điểm cần cải thiện:** pull trước khi sửa, chỉ sửa phần của mình thay vì viết lại cả file, thống nhất ai viết code ở mỗi checkpoint ngay từ đầu để CP2 không bị làm trùng, và thêm kiểm tra tự động sớm hơn (kiểm tra yaml chỉ có từ CP4). Vì code và bảng được viết với sự hỗ trợ của AI, mình cần luôn tự đọc lại và tự tính lại các số chính để giải thích được khi hội đồng hỏi.
- **Hạn chế:** phần C (bảng lỗi) và E (hồ sơ) do Đạo và Bảo làm; mình chỉ đối chiếu số liên quan đến A, B, D chứ chưa rà toàn bộ nội dung hai phần đó.
