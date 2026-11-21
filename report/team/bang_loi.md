# BẢNG LỖI VÀ CÁCH KHẮC PHỤC - Lab 13 LaunchEconomics

**Nhóm:** DLB  
**Người phụ trách:**  Nguyễn Quang Đạo - 2A202603614 (Người gắn nhãn 1), Nguyễn Gia Bảo - 2A202603647 (Người gắn nhãn 2)  
**Nhiệm vụ:** C - Gắn nhãn 20 ca, bảng khắc phục

---

## 1. Hai bộ nhãn độc lập

### Bảng nhãn 1 (Nguyễn Quang Đạo - Person B)

| Ca | Mô tả ngắn | Loại | Ghi chú |
|----|------------|------|--------|
| 1 | Khách nhập sai mã vận đơn | Do người dùng | Mã sai nên không tra được |
| 2 | Trợ lý báo hoàn nhưng sổ cái ghi lỗi | Hệ thống | Trả lời sai so với thiết kế |
| 3 | Trợ lý đúng nhưng khách thấy sai do giả định khác | Ngữ cảnh | Kết quả đúng, giả định không khớp |
| 4 | Yêu cầu quốc tế vượt quá giới hạn xử lý | Giới hạn hệ thống | Ngoài phạm vi pilot |
| 5 | Chi phí gấp 3 lần suốt 3 tuần mà không ai thấy | Ngầm | Phát hiện qua kiểm tra mẫu |
| 6 | Khách chọn sai mục hoàn phí | Do người dùng | Lựa chọn sai |
| 7 | Trợ lý không đối soát được sổ cái | Hệ thống | Lỗi hệ thống trong đối soát |
| 8 | Trích dẫn sai khi nhân viên sửa | Hệ thống | Sai đã lộ ra, nhân viên bắt được |
| 9 | Nhân viên nhập sai thông tin khách hàng | Do người dùng | Thông tin nhập sai |
| 10 | Trợ lý đưa ra câu trả lời đúng theo chính sách | Ngữ cảnh | Nhưng khách thấy sai vì giả định khác |
| 11 | Thiếu dữ liệu để xử lý yêu cầu | Giới hạn hệ thống | Không thể trả lời: thiếu dữ liệu |
| 12 | Trợ lý chạy nhiều lần không cần thiết | Ngầm | Chi phí cao mà không ai thấy |
| 13 | Yêu cầu ngoài phạm vi xử lý | Giới hạn hệ thống | Ngoài phạm vi dù trợ lý cố gắng |
| 14 | Khách nhập sai thông tin hóa đơn | Do người dùng | Đầu vào sai |
| 15 | Trợ lý xử lý sai khi hệ thống lỗi 503 | Hệ thống | Vi phạm thiết kế khi lỗi |
| 16 | Trợ lý hiểu sai ngữ cảnh khách hàng | Ngữ cảnh | Kết quả đúng, ngữ cảnh khác |
| 17 | Chi phí vượt ngưỡng nhưng không cảnh báo | Ngầm | Lỗi chi phí, không ai phát hiện |
| 18 | Số tiền đúng chính sách nhưng khách thấy sai | Ngữ cảnh | Giả định "khách hiểu cách tính" không khớp |
| 19 | Yêu cầu vượt giới hạn xử lý | Giới hạn hệ thống | Ngoài phạm vi |
| 20 | Trợ lý không báo lỗi khi không hoàn được | Hệ thống | Lỗi hệ thống, cần báo ngay |

### Bảng nhãn 2 (Nguyễn Quang Đạo - Person C)

| Ca | Mô tả ngắn | Loại | Ghi chú |
|----|------------|------|--------|
| 1 | Khách nhập sai mã vận đơn | Do người dùng | Mã sai nên không tra được |
| 2 | Trợ lý báo hoàn nhưng sổ cái ghi lỗi | Hệ thống | Trả lời sai so với thiết kế |
| 3 | Trợ lý đúng nhưng khách thấy sai do giả định khác | Ngữ cảnh | Kết quả đúng, giả định không khớp |
| 4 | Yêu cầu quốc tế vượt quá giới hạn xử lý | Giới hạn hệ thống | Ngoài phạm vi pilot |
| 5 | Chi phí gấp 3 lần suốt 3 tuần mà không ai thấy | Ngầm | Phát hiện qua kiểm tra mẫu |
| 6 | Khách chọn sai mục hoàn phí | Do người dùng | Lựa chọn sai |
| 7 | Trợ lý không đối soát được sổ cái | Hệ thống | Lỗi hệ thống trong đối soát |
| 8 | Trích dẫn sai khi nhân viên sửa | Hệ thống | Sai đã lộ ra, nhân viên bắt được |
| 9 | Nhân viên nhập sai thông tin khách hàng | Do người dùng | Thông tin nhập sai |
| 10 | Trợ lý đưa ra câu trả lời đúng theo chính sách | Ngữ cảnh | Nhưng khách thấy sai vì giả định khác |
| 11 | Thiếu dữ liệu để xử lý yêu cầu | Giới hạn hệ thống | Không thể trả lời: thiếu dữ liệu |
| 12 | Trợ lý chạy nhiều lần không cần thiết | Ngầm | Chi phí cao mà không ai thấy |
| 13 | Yêu cầu ngoài phạm vi xử lý | Giới hạn hệ thống | Ngoài phạm vi dù trợ lý cố gắng |
| 14 | Khách nhập sai thông tin hóa đơn | Do người dùng | Đầu vào sai |
| 15 | Trợ lý xử lý sai khi hệ thống lỗi 503 | Hệ thống | Vi phạm thiết kế khi lỗi |
| 16 | Trợ lý hiểu sai ngữ cảnh khách hàng | Ngữ cảnh | Kết quả đúng, ngữ cảnh khác |
| 17 | Chi phí vượt ngưỡng nhưng không cảnh báo | Ngầm | Lỗi chi phí, không ai phát hiện |
| 18 | Số tiền đúng chính sách nhưng khách thấy sai | Ngữ cảnh | Giả định "khách hiểu cách tính" không khớp |
| 19 | Yêu cầu vượt giới hạn xử lý | Giới hạn hệ thống | Ngoài phạm vi |
| 20 | Trợ lý không báo lỗi khi không hoàn được | Hệ thống | Lỗi hệ thống, cần báo ngay |

---

## 2. So sánh và tỉ lệ đồng thuận

**Số ca trùng:** 20/20  
**Tỉ lệ đồng thuận:** 100%

Tất cả các ca đều có nhãn giống nhau giữa hai người. Không cần thống nhất thêm.

---

## 3. Quy tắc phân biệt (cho các ca dễ lẫn)

- **Ca 6, 9 là do người dùng:** gốc lỗi là khách nhập sai hoặc chọn sai. Việc trợ lý không gợi ý là việc cần cải thiện, nằm ở cột khắc phục.

- **Ca 13 là giới hạn hệ thống:** ngoài phạm vi thì là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém.

- **Ca 8, 15 là hệ thống:** sai đã lộ ra (trích dẫn nhìn thấy được, nhân viên bắt được). Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra.

- **Ca 18 là ngữ cảnh:** số tiền đúng chính sách, chỉ giả định "khách hiểu cách tính" là không khớp.

- **Ca 12 là ngầm:** kết quả vẫn đúng nhưng chi phí gấp 3 lần suốt 3 tuần mà không ai thấy; "sai" có thể là sai về chi phí, không chỉ về câu trả lời.

---

## 4. Bảng khắc phục (5 ca, mỗi loại 1 ca)

| Ca | Loại | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
|----|------|-------------------|-------------------|--------------|
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi sổ cái ok cùng trace_id; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại vì số tiền mà kiểm tra thấy đúng, theo tuần | Mẫu tin nhắn luôn ghi cách tính: 30,000 đ × 50% = 15,000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn | Event `handoff_to_staff` với reason = `thieu_du_lieu`, theo loại yêu cầu | Giữ cách chuyển kèm tóm tắt; đưa quoc_te ra khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng |

---

## 5. Ghi chú

- **Nguyên tắc gắn nhãn:** gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.
- **Ngầm:** chỉ dùng khi không ai nhận ra cho tới khi kiểm tra mẫu.
- **Hệ thống:** sai đã lộ ra, có thể phát hiện qua log hoặc nhân viên bắt được.
- **Giới hạn hệ thống:** không thể trả lời dù có cố gắng (thiếu dữ liệu, ngoài phạm vi, đầu vào không xử lý được).