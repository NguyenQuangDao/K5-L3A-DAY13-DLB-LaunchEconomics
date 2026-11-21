# BẢNG CHI PHÍ - Lab 13 LaunchEconomics

**Nhóm:** DLB  
**Người phụ trách:** Nguyễn Quang Đạo - 2A202603614 (Viết bảng), Nguyễn Gia Bảo - 2A202603647 (Kiểm số)
**Nhiệm vụ:** A2, A3, B1-B4

---

## A2 · Chi phí mỗi việc thành công từ trace [simulated]

### Các khoản chi phí (tử số: MỌI lần chạy, kể cả lỗi)

| Khoản | Số tiền (đ) | Ghi chú |
|------|-------------|---------|
| Token (mọi lần chạy) | 245,585 | đo từ trace |
| Tool (5.600 lần gọi) | 84,000 | đo từ trace |
| Trong đó, lần chạy thứ 2 và 3 | 93,804 | đo từ trace |
| Xem lại (890 phút) | 1,780,000 | **simulated** |
| Làm lại (1,132 phút) | 2,264,000 | **simulated** |
| **Tổng chi phí** | **4,373,585** | có phần simulated |
| Số việc thành công | 978 | |
| **Chi phí mỗi việc thành công** | **4,472** | **simulated** |
| Hoá đơn token+tool / số yêu cầu | 274.7 | đo từ trace |

### Nhận xét

Chi phí mỗi việc thành công (**4,472 đ**) gấp **16.3 lần** hoá đơn token/chia số yêu cầu (**274.7 đ**).

Chi phí lớn nhất là **làm lại**, chiếm **51.8%** [simulated], tiếp theo là xem lại **40.7%** [simulated]. Giờ nhân viên (xem lại + làm lại) chiếm **92.5%** tổng chi phí.

Nếu so với nhân viên tự làm (12,000 đ/yc), chi phí trợ lý **0.37×**. Nếu tính cả phần chuyển nhân viên (222 yc không thành công), chi phí cả hệ thống mỗi yc là **5,865 đ = 0.49×**.

---

## A3 · Tách theo loại yêu cầu [simulated]

| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy/yêu cầu | Chi phí mỗi việc thành công | So với 12,000 đ |
|------|------------|-----------------|------------------|----------------------------|----------------|
| noi_dia | 824 | 95.0% | 1.112 | 2,696 đ | 0.225× |
| hang_nang | 158 | 74.1% | 1.468 | 8,221 đ | 0.685× |
| quoc_te | 150 | 27.3% | 2.320 | 22,515 đ | 1.876× |
| doi_tac | 68 | 54.4% | 1.882 | 10,215 đ | 0.851× |

### Tỉ lệ ok theo lần thử (chạy lại có giúp không?)

| Loại | Lần 1 | Lần 2 | Lần 3 |
|------|--------|--------|--------|
| noi_dia | 91.0% | 75.7% | 38.9% |
| hang_nang | 70.9% | 39.1% | 17.9% |
| quoc_te | 30.0% | 11.4% | 2.2% |
| doi_tac | 51.5% | 18.2% | 14.8% |

### Kết luận

- **quoc_te** không đáng để trợ lý xử lý: thành công chỉ 27.3%, chạy lại tới 3 lần không giúp (tỉ lệ ok giảm mạnh từ lần 1).
- **doi_tac** sát ngưỡng (0.85×) và có điều khoản riêng, nên cũng loại khỏi phạm vi pilot.
- **noi_dia** và **hang_nang** là phạm vi pilot phù hợp (0.23× và 0.69× so với 12,000 đ).

---

## B1 · Bảng độ nhạy (đổi từng yếu tố)

| Kịch bản | Chi phí mỗi việc thành công [sim] | Thay đổi |
|----------|-----------------------------------|----------|
| Gốc (A2) | 4,472 đ | - |
| Giá token gấp đôi | 4,723 đ | +5.6% |
| Giá token giảm một nửa | 4,346 đ | -2.8% |
| Xem lại gấp đôi | 6,292 đ | +40.7% |
| Xem lại giảm một nửa | 3,562 đ | -20.3% |
| Làm lại gấp đôi | 6,787 đ | +51.8% |
| Làm lại giảm một nửa | 3,315 đ | -25.9% |
| Lương tăng 25% | 5,506 đ | +23.1% |
| Tối đa 2 lần chạy | 4,237 đ | -5.2% |
| Chỉ 1 lần chạy | 4,111 đ | -8.1% |

### Xếp hạng 3 yếu tố ảnh hưởng mạnh nhất

1. **Số ca làm lại** (51.8%)
2. **Tỉ lệ xem lại** (40.7%)
3. **Lương nhân viên** (23.1%)

---

## B2 · Đổi một cặp và xếp hạng

Giá token gấp đôi + xem lại gấp đôi: **6,543 đ (+46.3%)**, đúng bằng tổng hai tác động riêng vì mô hình cộng tuyến tính.

**Xếp hạng:** 1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên.

---

## B3 · Giới hạn chạy lại có thật sự rẻ hơn? [simulated]

Chi phí cả hệ thống = tổng chi phí trợ lý + 12,000 đ × số yêu cầu không thành công.

| Giới hạn | Tổng trợ lý [sim] | Không thành công | Cả hệ thống | Chi phí mỗi việc thành công |
|----------|------------------|------------------|-------------|----------------------------|
| 1 lần | 3,621,781 đ | 319 | 7,449,781 đ | 4,111 đ (thấp nhất) |
| 2 lần | 4,093,220 đ | 234 | **6,901,220 đ (rẻ nhất)** | 4,237 đ |
| 3 lần | 4,373,585 đ | 222 | 7,037,585 đ | 4,472 đ |

- Giới hạn **2 lần rẻ nhất cho công ty** (6.9 triệu đ).
- Không trùng với giới hạn cho cps thấp nhất (1 lần: 4,111 đ).
- Tối ưu cps riêng sẽ đẩy thêm **85 việc** sang nhân viên.

---

## B4 · Nếu phải xem lại tất cả [simulated]

Chỉ lấy noi_dia + hang_nang (982 yêu cầu):

1. Yêu cầu có ít nhất một lần chạy ok: **948**, mỗi yêu cầu xem lại 5 phút → **9,480,000 đ**.
2. Số ca lam_lai: **48**, mỗi ca làm lại 9 phút → **864,000 đ**.
3. Token + tool của 982 yêu cầu: **224,513 đ**.
4. Tổng: **10,568,513 đ**, chia cho **900** việc thành công → **11,743 đ = 0.98×** của 12,000 đ.

### Độ nhạy theo phút làm lại

Cột `phut_lam_lai_simulated` trung bình **15.3 phút/ca** (trung vị 14.5). Thay 9 bằng 15.3:

48 × 15.3 × 2,000 = 1,468,800 đ → tổng **11,173,313 đ** → **12,414 đ = 1.03×** [simulated].

- **Mức hoà vốn:** mỗi lần xem lại phải ≤ 5.1 phút (với 9 phút làm lại) hoặc ≤ 4.8 phút (với 15.3 phút).
- Xem lại 100% thì trợ lý gần như không tiết kiệm được gì (chi phí xem lại chiếm 90%).
- Pilot phải học được tỉ lệ xem lại có thể giảm an toàn xuống mức nào.

---

## Bảng tổng hợp số đối chiếu

| Khoản | Số để đối chiếu |
|------|-----------------|
| cps (chi phí mỗi việc thành công) | 4,472 đ [simulated] |
| Gấp bao nhiêu lần hoá đơn token | 16.3× |
| Tỉ lệ làm lại trong tổng chi phí | 51.8% [simulated] |
| Tỉ lệ xem lại trong tổng chi phí | 40.7% [simulated] |
| Giờ nhân viên chiếm tổng chi phí | 92.5% [simulated] |
| cps trong phạm vi noi_dia + hang_nang | 3,414 đ [simulated] |
| cps cộng cố định (45.000 yc/tháng) | 4,599 đ [simulated] |
| cps cộng cố định (một nửa) | 5,784 đ [simulated] |
| chi phí cả hệ thống mỗi yc | 5,865 đ = 0.49× [simulated] |
