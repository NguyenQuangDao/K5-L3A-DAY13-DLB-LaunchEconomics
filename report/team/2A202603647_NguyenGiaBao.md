# Báo cáo cá nhân — NguyenGiaBao-2A202603647

## 1. Thông tin thành viên

- Họ tên: Nguyễn Gia Bảo
- MSSV: 2A202603647
- Email: 26ai.baong5@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ (Person C); kiểm số các số đưa vào hồ sơ

## 2. Phần việc phụ trách

- Giữ hồ sơ `report/team/ho_so_launch_v0.md`: điền dần bảy mục từ kết quả CP1–CP4, viết đề xuất cuối.
- Gắn nhãn độc lập 20 ca lỗi (CP3) với vai người gắn nhãn 2, so nhãn với người gắn nhãn 1, hoàn thiện `report/team/bang_loi.md`.
- Kiểm số: đối chiếu các số trong hồ sơ với output `src/lab13.py`, với dữ liệu gốc và với số đối chiếu trong hướng dẫn.

## 3. Đóng góp cụ thể

- **Hồ sơ launch v0 (PR #3):**
  - Đưa hồ sơ về đúng mẫu một trang, bảy mục.
  - Mỗi mục có con số chính, trạng thái hợp lệ (Xong, có bằng chứng · Chưa · Giả lập) và một vai trò phụ trách.
  - Gắn nhãn `[simulated]` ngay sau từng số dẫn xuất từ cột `_simulated`.
- **Sửa các điểm dễ bị trừ điểm trong bản hồ sơ trước:**
  - So với nhân viên tự làm: 0,37× [simulated] → 0,49× [simulated], vì phải cộng 222 yêu cầu nhân viên làm thay.
  - Bỏ câu "chỉ số chính cao hơn baseline 0,70", vì đợt chạy thử không có đối chứng.
  - Người phụ trách đổi từ tên người sang vai trò.
- **Mục 6 (pilot):**
  - Ghi rõ chỉ cách chia theo cụm (nhân viên, depot) mới thiếu mẫu cho mức chênh 5 điểm.
  - Mỗi nhánh 20 × 299 = 5.980 yêu cầu thực tế; với DE = 6,96, cỡ mẫu hiệu dụng ≈ 859 yêu cầu mỗi nhánh.
  - Nêu con số bất lợi: power 0,64 nếu tác động thật là 5 điểm.
- **Đề xuất Go có điều kiện:**
  - Nêu các con số bất lợi: power 0,64; xem lại 100% → 0,98× [simulated] đến 1,03× [simulated]; mở lại 7 ngày hiện tại 4,25%.
  - Mỗi điều kiện có vai trò phụ trách và ngày kiểm tra.
  - Ngưỡng hoà vốn ghi kèm giả định: ≤ 5,1 phút [simulated] xem lại nếu làm lại 9 phút/ca; ≤ 4,8 phút [simulated] nếu làm lại 15,3 phút/ca [simulated].
- **Bảng lỗi (PR #4):**
  - Gắn nhãn độc lập 20 ca trong 8 phút, không xem nhãn của người gắn nhãn 1.
  - So nhãn: trùng 19/20 = 95%. Ca 13 lệch: mình gắn Hệ thống, người gắn nhãn 1 gắn Giới hạn hệ thống.
  - Cùng người gắn nhãn 1 thống nhất ca 13 là Giới hạn hệ thống, theo nguyên tắc gắn theo nguyên nhân gốc. Cột nhãn của mình giữ nguyên như lúc gắn.
  - Xác nhận với người gắn nhãn 1 rằng bộ nhãn 1 được gắn độc lập trên đúng 20 ca của đề.
  - Bổ sung mẫu số và tần suất đếm cho cách phát hiện của ca 4, 7, 18; ghi nguồn bảng khắc phục.

## 4. Bằng chứng

- PR #3 (hồ sơ launch v0), commit `3e77a51`, `6b7ec23`, `753c0bb`.
- PR #4 (bảng lỗi), commit `24e0e2b`, `2c0780c`, `05565d3`.
- File: `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`.
- Bộ nhãn độc lập của mình: cột "Nhãn người 2" trong `bang_loi.md`.
- Phép kiểm số CP1, đối chiếu với output `lab13.py`:
  - 4.373.585 đ [simulated] ÷ 978 ≈ 4.472 đ [simulated]
  - (245.585 + 84.000) ÷ 1.200 ≈ 274,7 đ (đo từ trace)
  - 4.472 đ [simulated] ÷ 274,7 đ ≈ 16,3× [simulated]
- Phép tính kiểm các số đưa vào hồ sơ PR #3:
  - Cỡ mẫu hiệu dụng: 5.980 ÷ (1 + 298 × 0,02) = 5.980 ÷ 6,96 ≈ 859.
  - Hoà vốn khi làm lại 9 phút/ca: (12.000 × 900 − 48 × 9 × 2.000 − 224.513) ÷ (948 × 2.000) ≈ 5,1 phút [simulated].
  - Hoà vốn khi làm lại 15,3 phút/ca [simulated]: (12.000 × 900 − 48 × 15,3 × 2.000 − 224.513) ÷ (948 × 2.000) ≈ 4,8 phút [simulated].
  - 15,3 phút/ca [simulated] là trung bình cột `phut_lam_lai_simulated` trên toàn bộ 74 ca `lam_lai` của mẫu; đây là kịch bản dùng trong hồ sơ PR #3: 12.415 đ [simulated] = 1,03× [simulated].
- Chênh lệch B4 đã gặp trong lúc làm: `lab13.py` bản commit `d3206b5` lấy trung bình trên 48 ca `lam_lai` trong phạm vi noi_dia + hang_nang: 16,25 phút/ca [simulated] → 12.516 đ [simulated] = 1,04× [simulated], lệch với hồ sơ PR #3. Khi đối chiếu hai nguồn (Claude Code đọc code và tính lại), nguyên nhân là phạm vi lấy trung bình phút làm lại: 74 ca toàn mẫu so với 48 ca trong phạm vi pilot. Cả hai kịch bản đều cho chi phí cao hơn mức nhân viên tự làm khi phải xem lại 100%, nên kết luận về B4 trong đề xuất không đổi.
- Từ commit `f531cc7`, `lab13.py` dùng 15,3 phút/ca [simulated] và in 12.415 đ [simulated] = 1,03× [simulated], khớp hồ sơ PR #3.
- Phát hiện khi chạy lại `lab13.py` trên máy Windows: lỗi `UnicodeEncodeError` khi in tiếng Việt; chạy được sau khi đặt `$env:PYTHONIOENCODING = "utf-8"`.

## 5. Công cụ AI đã dùng

- **Claude Code**, dùng vào các việc:
  - Đọc đề và lập hướng dẫn từng bước cho vai Person C.
  - Chạy lại `lab13.py` và một script kiểm tra tạm để tính lại các số B1–B4, D1, E1 trên dữ liệu.
  - Soạn và chỉnh nội dung `ho_so_launch_v0.md`, `bang_loi.md`.
  - Tạo commit và PR.
- **Codex**: review độc lập các thay đổi qua nhiều vòng. Codex bắt được câu "không cách chia nào đủ mẫu" nói quá rộng, câu ví dụ ca 7 dễ hiểu nhầm, và việc mục 5 ghi "thống nhất" trước khi hai người xác nhận.
- **Không dùng AI để gắn nhãn:** 20 nhãn ở cột người 2 là mình tự gắn theo mô tả ca trong đề; AI chỉ đưa định nghĩa năm loại và thứ tự câu hỏi để phân loại.
- **Phần mình trực tiếp làm khi kiểm tra:**
  - Gắn nhãn, so hai bộ nhãn, hỏi lại người gắn nhãn 1 về nguồn bộ nhãn 1 và chốt ca 13.
  - Đọc từng góp ý review, quyết định áp dụng hay không; ví dụ dùng grep (qua Claude Code) kiểm lại một cảnh báo của Codex về từ bị cấm trong hồ sơ và xác nhận cảnh báo đó sai.
- **Nguồn đối chiếu của từng nhóm số:**
  - Số A1–A4 trong hồ sơ: đối chiếu với output `lab13.py`.
  - Số B1–B4, D1, E1 trong hồ sơ PR #3: Claude Code chạy một script tạm trên hai file CSV để tính lại và so với số đối chiếu trong hướng dẫn.
  - Các phép kiểm cụ thể được ghi ở mục 4: chi phí mỗi việc thành công (tử số, mẫu số, kết quả), cỡ mẫu hiệu dụng và hai ngưỡng hoà vốn. Các phép này do Claude Code tính theo yêu cầu của mình, sau đó được Codex review độc lập trước khi đưa vào hồ sơ.

## 6. Tự đánh giá

- **Làm tốt:**
  - Hồ sơ giữ đúng khung bảy mục và nêu đủ con số bất lợi kèm cách xử lý, đúng tiêu chí C6 của hội đồng.
  - Hai bộ nhãn được giữ độc lập; ca lệch được xử lý minh bạch, có xác nhận của người gắn nhãn 1.
- **Hạn chế:**
  - Ca 13 mình gắn theo hành vi của trợ lý (trả lời chung chung), chưa theo nguyên nhân gốc (yêu cầu ngoài phạm vi). Bài học: hỏi "gốc lỗi ở đâu" trước khi hỏi "trợ lý làm sai gì".
  - Hồ sơ cần nhiều vòng review mới chốt được; lần sau nên thống nhất mẫu với nhóm từ đầu buổi để tránh hai người cùng sửa một file.
  - B1–B4 hiện đã có trong `lab13.py`, nhưng D1 và E1 chưa được in khi chạy; số D1, E1 trong hồ sơ đang dựa trên script tạm và phép tính tay.
  - Kịch bản B4 từng lệch giữa hồ sơ và `lab13.py` (15,3 so với 16,25 phút/ca [simulated]); nhóm đã thống nhất về 15,3 phút/ca từ commit `f531cc7`, chi tiết ở mục 4. Bài học: đối chiếu code với hồ sơ ngay sau mỗi lần một trong hai thay đổi.
