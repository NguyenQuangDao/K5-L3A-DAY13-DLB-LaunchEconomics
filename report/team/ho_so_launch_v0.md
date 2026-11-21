# HỒ SƠ LAUNCH V0 - Lab 13 LaunchEconomics

**Nhóm:** DLB  
**Người phụ trách:** Nguyễn Quang Đạo (2A202603614 - Person B)  
**Ngày tạo:** 21/11/2026  
**Đề xuất:** Go có điều kiện

---

## 1. Chi phí mỗi việc thành công

| Khoản | Số liệu | Trạng thái | Người phụ trách |
|------|---------|------------|-----------------|
| cps (chi phí mỗi việc thành công) | 4,472 đ [simulated] | Giả lập | Nguyễn Quang Đạo |
| cps trong phạm vi noi_dia + hang_nang | 3,414 đ [simulated] | Giả lập | Nguyễn Quang Đạo |
| cps cộng cố định (45,000 yc/tháng) | 4,599 đ [simulated] | Giả lập | Nguyễn Quang Đạo |
| cps cộng cố định (một nửa) | 5,784 đ [simulated] | Giả lập | Nguyễn Quang Đạo |
| cps cả hệ thống mỗi yc | 5,865 đ = 0.49× của 12,000 đ [simulated] | Giả lập | Nguyễn Quang Đạo |
| Chi phí cố định mỗi việc (45,000 yc) | 1,185 đ [simulated] | Giả lập | Nguyễn Quang Đạo |

**Kết luận:** Chi phí mỗi việc thành công bằng **0.37×** so với nhân viên tự làm (12,000 đ).

---

## 2. Ba yếu tố nhạy nhất

| STT | Yếu tố | Độ nhạy | Trạng thái |
|-----|--------|---------|------------|
| 1 | Số ca làm lại | +51.8% / -25.9% | Giả lập |
| 2 | Tỉ lệ xem lại | +40.7% / -20.3% | Giả lập |
| 3 | Lương nhân viên | +23.1% | Giả lập |

**Kết luận:** Pilot phải theo dõi **tỉ lệ làm lại** và **tỉ lệ xem lại** để kiểm soát chi phí.

---

## 3. So với nhân viên tự làm

| Khoản | Số liệu | Trạng thái |
|------|---------|------------|
| cps / 12,000 đ | 0.37× | Giả lập |
| cps trong phạm vi / 12,000 đ | 0.28× | Giả lập |
| cps cả hệ thống / 12,000 đ | 0.49× | Giả lập |

**Kết luận:** Trợ lý tiết kiệm được **63%** chi phí so với nhân viên tự làm (nếu chỉ tính trong phạm vi pilot: 72%).

---

## 4. Chỉ số

| Loại | Chỉ số | Giá trị | Trạng thái |
|------|--------|---------|------------|
| Chính | % đóng trong 24h và không mở lại 7 ngày | 82.83% | Đo từ trace |
| Dùng | Tỉ lệ bỏ qua gợi ý | 27.12% | Đo từ trace |
| An toàn | Tỉ lệ lỗi lọt đến khách (mở lại 7 ngày) | 4.25% | Đo từ trace |

**Kết luận:** Tất cả chỉ số đều tốt:
- Chỉ số chính 82.83% cao hơn baseline 0.70.
- Tỉ lệ bỏ qua gợi ý 27.12% acceptable.
- Tỉ lệ lỗi lọt 4.25% acceptable.

---

## 5. Bảng lỗi và cách khắc phục

| Loại | Số ca | Tỉ lệ | Trạng thái |
|------|-------|-------|------------|
| Do người dùng | 4 | 20% | Giả lập |
| Hệ thống | 5 | 25% | Giả lập |
| Ngữ cảnh | 4 | 20% | Giả lập |
| Giới hạn hệ thống | 4 | 20% | Giả lập |
| Ngầm | 3 | 15% | Giả lập |
| **Tổng** | **20** | **100%** | |

**Tỉ lệ đồng thuận:** 100% (20/20 ca)

**Khắc phục:** Đã điền 5 ca (mỗi loại 1 ca) trong bang_loi.md.

---

## 6. Pilot plan

| Khoản | Giá trị | Trạng thái |
|------|--------|------------|
| Scope | noi_dia + hang_nang | Đã xác định |
| Assignment | 20 + 20 nhân viên | Đã xác định |
| Rollout | 0.10 -> 0.25 -> 0.50 | Đã xác định |
| primary_metric | dong_trong_24h_khong_mo_lai_7_ngay | Đã xác định |
| MDE | 0.06 (6 điểm) | Đã chấp nhận |
| N mỗi nhóm | 859 | Đủ |
| Luật dừng | 4 luật đủ 4 vế | Có |

**Kết luận:** Pilot plan đầy đủ, đủ mẫu (859), có 4 luật dừng đúng mẫu, có luật an toàn.

---

## 7. Rủi ro kinh tế

| Rủi ro | Tác động | Dấu hiệu | Hành động | Người phụ trách |
|--------|---------|----------|-----------|-----------------|
| Làm lại tăng gấp đôi | cps lên 6,787 đ | Tỉ lệ làm lại > 7% | Thu hẹp về noi_dia | PM trợ lý hoàn phí |
| Xem lại 100% | cps lên 11,743 đ = 0.98× | % xem lại > 50% | Giảm xem lại theo bậc | Trưởng nhóm CSKH |
| Khối lượng thấp | cố định +1,185 đ/việc | Việc thành công < 50% kế hoạch | Xem lại hợp đồng cố định | PM trợ lý hoàn phí |

**Kết luận:** Có 3 rủi ro kinh tế rõ ràng, mỗi rủi ro có dấu hiệu theo dõi và hành động cụ thể.

---

## 8. Đề xuất

**Đề xuất: Go có điều kiện**

### Điều kiện 1: Sửa lỗi hệ thống
- **Nội dung:** Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20)
- **Người phụ trách:** Kỹ sư trưởng agent
- **Ngày kiểm tra:** Trước ngày bắt đầu pilot (2027-01-05)

### Điều kiện 2: Chấp nhận mức chênh 6 điểm
- **Nội dung:** Giám đốc vận hành ký chấp nhận mức chênh 6 điểm (power 0.64 ở mức 5 điểm)
- **Người phụ trách:** Giám đốc vận hành
- **Ngày kiểm tra:** Trước ngày bắt đầu pilot (2027-01-05)

### Điều kiện 3: Bật đủ event có trace_id
- **Nội dung:** Thay phút simulated bằng phút đo thật sau tuần 1
- **Người phụ trách:** PM trợ lý hoàn phí
- **Ngày kiểm tra:** Tuần đầu pilot

### Điều kiện 4: Có kế hoạch giảm xem lại theo bậc
- **Nội dung:** Vì xem lại 100% thì không tiết kiệm (B4)
- **Người phụ trách:** Trưởng nhóm CSKH
- **Ngày kiểm tra:** Tuần đầu pilot

---

## 9. Kết luận

Với các điều kiện trên được đáp ứng, pilot có thể bắt đầu với:
- Chi phí tiết kiệm 63% so với nhân viên tự làm.
- Chỉ số chính cao hơn baseline (82.83% > 70%).
- Có hệ thống cảnh báo và dừng khi rủi ro tăng cao.

**Người phê duyệt:** Giám đốc vận hành LogiX-VN  
**Ngày phê duyệt:** 21/11/2026