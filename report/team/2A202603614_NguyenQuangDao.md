# Báo cáo cá nhân - Nguyễn Quang Đạo

## MSSV: 2A2603614

### Vai trò trong nhóm

- **CP1 (Kiểm số)**: Kiểm tra tính đúng đắn của các phép tính trong Nhiệm vụ A và B
- **CP2 (Viết bảng độ nhạy)**: Thực hiện toàn bộ bảng B1-B4 và phân tích độ nhạy
- **CP3 (Người gắn nhãn 1)**: Độc lập gắn nhãn 20 ca lỗi, so nhãn với người thứ hai, đạt tỉ lệ đồng thuận 95%
- **Quản lý hồ sơ**: Đóng góp nội dung cho toàn bộ hồ sơ launch v0

---

## Nhiệm vụ A: Mô hình chi phí (Đóng góp kiểm số)

### A1 - Ba phép thử đáp án biết trước
- **Công việc**: Kiểm tra 3 hàm số trong `lab13_starter.py` bằng cách chạy tay và so sánh kết quả
- **Kết quả đạt**:
  - Số lần chạy trung bình, tối đa 2 lần: **1,20** ✓
  - Số lần chạy trung bình, chạy đến khi đúng: **1,25** ✓
  - Hệ số chi phí mỗi việc thành công, tối đa 3 lần: **1,25** ✓ (bằng 1/p vì k triệt tiêu)

### A2 - Chi phí từ trace
- **Công việc**: Kiểm tay toàn bộ bảng chi phí, đặc biệt chú ý:
  - Đảm bảo **tử số tính MỌI lần chạy** (kể cả lỗi)
  - Mẫu số chỉ đếm yêu cầu có `ket_qua == 'thanh_cong'` (978 yêu cầu)
  - Tách biệt các khoản đo từ trace vs giả lập `_simulated`
- **Các con số đã kiểm**:
  - Token: **245.585 đ** (đo từ trace)
  - Tool: **84.000 đ** (5.600 lần gọi × 15 đ/lần)
  - Xem lại: **1.780.000 đ** (890 phút × 2.000 đ/phút) [simulated]
  - Làm lại: **2.264.000 đ** (1.132 phút × 2.000 đ/phút) [simulated]
  - Tổng chi phí: **4.373.585 đ**
  - Chi phí mỗi việc thành công: **4.472 đ** [simulated]
- **Phát hiện**: Chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn token/chia số yêu cầu (274.7 đ), do bỏ sót chi phí nhân viên nếu không tính xem lại và làm lại

### A3 - Tách theo loại yêu cầu
- **Công việc**: Xác nhận kết quả cho 4 loại yêu cầu:
  - **noi_dia**: 2.696 đ (0.225×), thành công 95.0%
  - **hang_nang**: 8.221 đ (0.685×), thành công 74.1%
  - **quoc_te**: 22.515 đ (1.876×), thành công 27.3% → **loại khỏi pilot**
  - **doi_tac**: 10.215 đ (0.851×), thành công 54.4% → **loại khỏi pilot**
- **Phân tích chạy lại**: Kiểm tra tỉ lệ ok theo lần thử, xác định chạy lại không giúp với quoc_te (30%→11.4%→2.2%)

### A4 - Chi phí cố định
- **Công việc**: Xác nhận cách tính chi phí cố định 40 triệu đ/tháng
  - Tỉ lệ thành công trong phạm vi: 900/1.200 → 33.750 việc/tháng (quy mô đầy đủ)
  - Chi phí cố định mỗi việc: 40.000.000/33.750 = **1.185 đ**
  - Tổng tại 45.000 yc/tháng: **4.599 đ** (3.414 + 1.185)
  - Tổng tại một nửa khối lượng: **5.784 đ** (3.414 + 2.370)

---

## Nhiệm vụ B: Bảng độ nhạy (Đóng góp chính)

### B1 - Đổi từng yếu tố
- **Công việc**: Viết và chạy toàn bộ bảng với 9 kịch bản, mỗi lần gọi `mo_hinh()` với đúng một tham số thay đổi
- **Kết quả chính**:
  | Kịch bản | Chi phí [simulated] | Thay đổi |
  |---|---:|---:|
  | Gốc | 4.472 đ | - |
  | Giá token gấp đôi | 4.723 đ | +5.6% |
  | Xem lại gấp đôi | 6.292 đ | +40.7% |
  | Làm lại gấp đôi | 6.787 đ | **+51.8%** |
  | Lương tăng 25% | 5.506 đ | +23.1% |
  | Giới hạn 2 lần | 4.237 đ | -5.2% |
  | Giới hạn 1 lần | 4.111 đ | -8.1% |
- **Kiểm tra**: Mỗi kịch bản "giảm một nửa" có mức giảm đúng bằng **nửa** mức tăng của "gấp đôi" (5.6→2.8; 40.7→20.3; 51.8→25.9), xác nhận tính tuyến tính của mô hình

### B2 - Đổi cặp và xếp hạng
- **Công việc**: Xếp hạng 3 yếu tố ảnh hưởng mạnh nhất
- **Kết quả**: 
  1. **Số ca làm lại** (+51.8%)
  2. **Tỉ lệ xem lại** (+40.7%)
  3. **Lương nhân viên** (+23.1%)
- **Ghi chú**: Giá token chỉ ảnh hưởng +5.6%, không phải yếu tố nhạy nhất

### B3 - Giới hạn chạy lại
- **Công việc**: Tính chi phí cả hệ thống (trợ lý + nhân viên làm thay)
- **Kết quả**:
  | Giới hạn | Trợ lý | Không thành công | Cả hệ thống | cps |
  |---|---:|---:|---:|---:|
  | 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
  | 2 lần | 4.093.220 đ | 234 | **6.901.220 đ** | 4.237 đ |
  | 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |
- **Phát hiện quan trọng**: Giới hạn **2 lần** rẻ nhất cho công ty, khác với giới hạn cho cps thấp nhất (1 lần). Tối ưu riêng cps đẩy thêm **85 việc** sang nhân viên

### B4 - Xem lại 100%
- **Công việc**: Tính chi phí nếu tất cả yêu cầu trong phạm vi đều phải xem lại
- **Kết quả**:
  - Với giả định đề bài (9 phút/ca làm lại): **11.743 đ = 0.98×** của 12.000 đ
  - Với dữ liệu thực (15.3 phút/ca làm lại): **12.415 đ = 1.03×**
- **Kết luận**: Xem lại 100% thì trợ lý **đắt hơn** nhân viên tự làm. Mức hoà vốn: mỗi lần xem lại phải ≤ 5.1 phút (làm lại 9 phút) hoặc ≤ 4.8 phút (làm lại 15.3 phút)

---

## Nhiệm vụ C: Bảng lỗi (Đóng góp chính)

### Gắn nhãn 20 ca độc lập
- **Quy trình**: Độc lập gắn nhãn 20 ca trong 8 phút, không trao đổi với người thứ hai
- **Tỉ lệ đồng thuận**: **95%** (19/20 ca)

### Phân biệt các ca dễ lẫn
- **Ca 13**: Ban đầu người 2 ghi "Hệ thống", tôi ghi "Giới hạn hệ thống". Sau thống nhất: **Giới hạn hệ thống** vì gốc lỗi là yêu cầu nằm ngoài phạm vi (bảo hiểm đối tác)
- **Quy tắc phân biệt ghi trong bang_loi.md**: "Gốc lỗi là yêu cầu nằm ngoài phạm vi trợ lý, nên là Giới hạn hệ thống; việc trợ lý trả lời chung chung là việc cần khắc phục"

### Bảng khắc phục 5 ca
- **Chọn 5 ca đại diện** (mỗi loại 1 ca):
  - **Ca 9 (Do người dùng)**: PM trợ lý hoàn phí, nhận diện mã sàn TMĐT
  - **Ca 7 (Hệ thống)**: Kỹ sư trưởng agent, đối soát sổ cái mỗi giờ
  - **Ca 18 (Ngữ cảnh)**: Trưởng nhóm CSKH, ghi cách tính vào mẫu tin nhắn
  - **Ca 4 (Giới hạn hệ thống)**: PM trợ lý hoàn phí, đưa quoc_te ra khỏi pilot
  - **Ca 17 (Ngầm)**: Kế toán trưởng, kiểm tra mẫu 100 đơn/tuần

---

## Nhiệm vụ D: Pilot plan

### Tính cỡ mẫu
- **Công việc**: Xác nhận 5 câu D1 bằng tay:
  - **a.** Chia theo yêu cầu: **1.251** mỗi nhóm
  - **b.** Theo nhân viên, m=75: **3.103** mỗi nhóm → **84 > 40 người** (không đủ)
  - **c.** 20 nhân viên mỗi nhóm: tối đa **1.000 < 1.251** (không đạt)
  - **e.** Mức chênh 6 điểm với 20 người: **m ≥ 299** yêu cầu/người

### Lựa chọn phương án
- **Chọn chia theo nhân viên, 20+20**, chấp nhận mức chênh 6 điểm thay vì 5 điểm (power giảm xuống ~0.64)
- **Lý do**: Đủ cụm mỗi nhóm (20), chia ngẫu nhiên, dễ theo dõi tác động

### Luật dừng
- **Luật 1** (An toàn): NẾU mở lại 7 ngày cao hơn đối chứng ≥2 điểm hoặc vượt 6%, THÌ Giám đốc vận hành tắt trợ lý trong 30 phút
- **Luật 2** (Chi phí): NẾU cps > 8.000 đ trong 2 tuần liên tiếp, THÌ PM thu hẹp về noi_dia và giới hạn 2 lần
- **Luật 3** (Dùng thử): NẾU tỉ lệ bỏ qua gợi ý > 40% trong 1 tuần, THÌ Trưởng nhóm CSKH phỏng vấn 5 nhân viên

---

## Nhiệm vụ E: Chỉ số, rủi ro, hồ sơ launch v0

### Chỉ số
- **Chính**: % đóng trong 24h và không mở lại 7 ngày: **82,83%** (994/1.200)
- **Dùng**: Tỉ lệ bỏ qua gợi ý: **27,12%** (48/177)
- **An toàn**: Tỉ lệ lỗi lọt đến khách: **4,25%** (51/1.200)

### Rủi ro kinh tế
- **Làm lại tăng gấp đôi**: +51.8%, lên 6.787 đ → giám sát tỉ lệ làm lại >7%
- **Xem lại 100% kéo dài**: 11.743 đ = 0.98× → giảm xem lại khi tỉ lệ sửa+bỏ <15%
- **Khối lượng thấp**: cố định tăng gấp đôi → xem lại hợp đồng

### Đề xuất Go có điều kiện
- Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20)
- Giám đốc vận hành ký chấp nhận mức chênh 6 điểm
- Bật đủ event có trace_id; thay phút simulated bằng phút đo thật sau tuần 1
- Có kế hoạch giảm xem lại theo bậc

---

## Bằng chứng đóng góp

| File | Nội dung |
|---|---|
| `report/team/bang_chi_phi.md` | Bảng B1-B4 hoàn chỉnh, có xếp hạng 3 yếu tố, B3 và B4 chi tiết |
| `report/team/bang_loi.md` | Hai bộ nhãn (95% đồng thuận), quy tắc phân biệt, bảng 5 ca khắc phục |
| `report/team/chi_so.md` | Chỉ số chính, dùng, an toàn; danh sách 10 event |
| `report/team/ho_so_launch_v0.md` | Hồ sơ launch v0 một trang, đề xuất Go có điều kiện |
| `report/team/phieu_cham.md` | Phiếu chấm nhóm khác |
| `src/lab13.py` | Code A1-A4, B1-B4 |

---

## Kinh nghiệm rút ra

1. **Chi phí nhân viên chiếm 92,5%** - Không thể bỏ qua xem lại và làm lại
2. **Chạy lại không giúp** với quoc_te (tỉ lệ ok giảm mạnh), cần xác định rõ nguyên nhân
3. **Giới hạn 2 lần rẻ nhất** cho công ty, nhưng tối ưu cps riêng sẽ đẩy thêm việc sang nhân viên
4. **Xem lại 100% thì đắt hơn** nhân viên tự làm → pilot cần giảm tỉ lệ xem lại
5. **Tính đúng mô hình chi phí** requires tử số = MỌI lần chạy, mẫu = chỉ thành công