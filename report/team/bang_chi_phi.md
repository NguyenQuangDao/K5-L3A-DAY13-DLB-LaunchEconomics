# BẢNG CHI PHÍ - Lab 13 LaunchEconomics

**Nhóm:** DLB  
**Người phụ trách:** Nguyễn Quang Đạo - 2A202603614 (Viết bảng), Nguyễn Gia Bảo - 2A202603647 (Kiểm số)  
**Nhiệm vụ:** A1-A4 (CP1), B1-B4 (CP2)

Số tính bằng `src/lab13.py` (chạy `cd src && python lab13.py`). Mọi con số tính từ cột `_simulated` ghi nhãn **simulated**.

---

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT (bằng 1/p vì k triệt tiêu) |

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

Khi so với nhân viên tự làm (12,000 đ/yc), không dùng trực tiếp 4,472 đ vì con số này chưa tính phần nhân viên làm thay 222 yêu cầu không thành công (148 chuyển nhân viên + 74 làm lại). Chi phí cả hệ thống mỗi yêu cầu là (4,373,585 + 222 × 12,000) / 1,200 = **5,865 đ = 0.49×** của 12,000 đ [simulated].

---

## A3 · Tách theo loại yêu cầu [simulated]

| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy/yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12,000 đ [simulated] |
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
- **noi_dia** và **hang_nang** là phạm vi pilot phù hợp (0.225× và 0.685× so với 12,000 đ) [simulated].

---

## A4 · Chi phí cố định 40 triệu đ/tháng (phạm vi noi_dia + hang_nang) [simulated]

Chi phí mỗi việc thành công trong phạm vi (chưa cộng cố định): 3,072,513 / 900 = **3,414 đ** [simulated].

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12,000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45,000 yêu cầu/tháng | 33,750 (= 45,000 × 900 ÷ 1,200) | 1,185 đ (= 40,000,000 ÷ 33,750) | 4,599 đ [simulated] (3,414 + 1,185) | 0.38× |
| Một nửa khối lượng | 16,875 | 2,370 đ | 5,784 đ [simulated] (3,414 + 2,370) | 0.48× |

- Chi phí cố định không đổi kết luận: ở cả hai mức khối lượng, phạm vi noi_dia + hang_nang vẫn rẻ hơn nhân viên tự làm (0.38× và 0.48×) [simulated].
- Nhưng cố định tăng gấp đôi khi khối lượng giảm một nửa (+1,185 đ → +2,370 đ mỗi việc), nên hồ sơ phải ghi rõ con số đã cộng cố định hay chưa, ở khối lượng nào.

---

## B1 · Đổi từng yếu tố [simulated]

Mỗi kịch bản là một lần gọi `mo_hinh(runs, reqs, ...)` trong `src/lab13.py` với đúng một tham số đổi. Gốc (A2) = 4,472 đ mỗi việc thành công [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1,000 token; giá tool giữ nguyên | 4,723 đ | +5.6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4,346 đ | -2.8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6,292 đ | +40.7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3,562 đ | -20.3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6,787 đ | +51.8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3,315 đ | -25.9% |
| Lương nhân viên tăng 25% | 2,500 đ mỗi phút | 5,506 đ | +23.1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien (0 phút xem lại, làm lại) | 4,237 đ | -5.2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4,111 đ | -8.1% |

Tự kiểm tra (code in `ĐẠT`): mỗi dòng "giảm một nửa" bằng đúng nửa mức tăng của dòng "gấp đôi" (5.6 → 2.8; 40.7 → 20.3; 51.8 → 25.9), vì mô hình cộng tuyến tính.

## B2 · Đổi một cặp và xếp hạng [simulated]

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6,543 đ (+46.3%)**, đúng bằng 5.6% + 40.7% vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. số ca làm lại (+51.8%) · 2. tỉ lệ xem lại (+40.7%) · 3. lương nhân viên (+23.1%)**; giá token chỉ +5.6%.
- Pilot phải theo dõi tỉ lệ làm lại và tỉ lệ xem lại, không phải giá token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn [simulated]

Chi phí cả hệ thống = tổng chi phí trợ lý + 12,000 đ × số yêu cầu không thành công (nhân viên phải làm thay).

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3,621,781 đ | 319 | 7,449,781 đ | 4,111 đ (thấp nhất) |
| 2 lần | 4,093,220 đ | 234 | **6,901,220 đ (rẻ nhất)** | 4,237 đ |
| 3 lần | 4,373,585 đ | 222 | 7,037,585 đ | 4,472 đ |

- Giới hạn **2 lần rẻ nhất cho công ty** (6,901,220 đ), rẻ hơn 3 lần 136,365 đ và rẻ hơn 1 lần 548,561 đ [simulated].
- **Không trùng** với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4,111 đ).
- Tối ưu riêng chi phí mỗi việc thành công sẽ đẩy thêm **85 việc** (319 − 234) sang nhân viên.

## B4 · Nếu phải xem lại tất cả [simulated]

Phạm vi `noi_dia` + `hang_nang` (982 yêu cầu, 900 việc thành công):

| Bước | Cách tính | Số tiền |
| --- | --- | ---: |
| Xem lại | 948 yêu cầu có ít nhất một lần chạy ok × 5 phút × 2,000 đ | 9,480,000 đ |
| Làm lại (đề: 9 phút/ca) | 48 ca lam_lai × 9 phút × 2,000 đ | 864,000 đ |
| Làm lại (dữ liệu: 15.3 phút/ca) | 48 × 15.3 × 2,000 đ | 1,468,800 đ |
| Token + tool | mọi lần chạy của 982 yêu cầu | 224,513 đ |
| **Tổng, làm lại 9 phút** | ÷ 900 việc thành công | 10,568,513 đ → **11,743 đ = 0.98×** |
| **Tổng, làm lại 15.3 phút** | ÷ 900 việc thành công | 11,173,313 đ → **12,415 đ = 1.03×** |

- Xem lại 100% thì chi phí mỗi việc thành công là **11,743 đ = 0.98×** của 12,000 đ [simulated]; nếu làm lại đúng như dữ liệu (15.3 phút, trung vị 14.5) thì **12,415 đ = 1.03×**, tức đắt hơn nhân viên tự làm.
- Mức hoà vốn: mỗi lần xem lại phải ≤ **5.1 phút** (làm lại 9 phút) hoặc ≤ **4.8 phút** (làm lại 15.3 phút), trong khi đề cho 5 phút.
- Xem lại chiếm khoảng 90% chi phí, nên pilot phải học được tỉ lệ xem lại có thể giảm an toàn xuống mức nào và mỗi lần xem lại có ngắn hơn 5 phút được không.

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
