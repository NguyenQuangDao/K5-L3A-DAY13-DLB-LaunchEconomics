# CHỈ SỐ VÀ RỦI RO KINH TẾ - Lab 13 LaunchEconomics

**Nhóm:** DLB  
**Người phụ trách:** Nguyễn Gia Bảo - 2A202603647 (Đặc tả), Nguyễn Quang Đạo - 2A202603614 (Kiểm số)
**Nhiệm vụ:** E - Đặc tả chỉ số, danh sách event, rủi ro kinh tế

---

## 1. Đặc tả chỉ số (tính thử trên 1,200 yêu cầu)

| Loại | Chỉ số | Tính thử | Ghi chú |
|------|--------|----------|---------|
| **Chính** | % đóng trong 24 giờ và không mở lại trong 7 ngày | 82.83% (994/1,200) | chỉ số chính |
| **Dùng** | Tỉ lệ bỏ qua gợi ý (sua + bo) / số được xem lại | 27.12% (48/177) | chỉ số dùng |
| **An toàn** | Tỉ lệ lỗi lọt đến khách: mở lại trong 7 ngày | 4.25% (51/1,200) | chỉ số an toàn |
| **Dùng (đề xuất)** | % yêu cầu mở bằng trợ lý | 75.00% | đề xuất thêm |
| **An toàn (đề xuất)** | % đơn hoàn sai tiền qua kiểm tra mẫu | 0.50% | đề xuất thêm |

### Ghi chú về chỉ số

- **Chỉ số chính trong đợt chạy thử là 82.83%**, không viết "trợ lý đã nâng chỉ số từ 0.70" vì đợt chạy thử không có nhóm đối chứng.
- **Tỉ lệ mở lại hiện tại là 4.25%** (51/1,200); trong phạm vi noi_dia + hang_nang là 3.97%.
- Để so sánh với nhóm đối chứng, đặt ngưỡng chênh 2 điểm (tức mở lại cao hơn 2% thì là vấn đề).

---

## 2. Danh sách event (tối thiểu 6, mỗi event có trace_id)

| Event | Ai tạo | Thuộc tính chính | Thời điểm | Dùng để tính chỉ số |
|-------|--------|------------------|-----------|---------------------|
| refund_request_created | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi | Tất cả |
| agent_run_completed | Agent | attempt, tokens_in/out, tool_calls, status, trace_id | Sau mỗi lần chạy | cps, token, tool |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra | bỏ qua gợi ý |
| staff_review_decision | Nhân viên | giu/sua/bo, phut_xem_lai (đo thật), trace_id | Khi bấm gửi/sửa/bỏ | xem_lai |
| staff_rework_completed | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi làm lại xong | lam_lai |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ | đối soát |
| handoff_to_staff | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên | chuyển nhân viên |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng | đóng trong 24h |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi mở lại | mở lại 7 ngày |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần | lỗi lọt |

**Kiểm tra chéo:** Với mỗi chỉ số, chỉ ra event nào dùng để tính:
- **Chính (đóng trong 24h, không mở lại 7 ngày):** refund_request_created, ticket_closed, ticket_reopened
- **Dùng (bỏ qua gợi ý):** agent_suggestion_shown, staff_review_decision
- **An toàn (lỗi lọt đến khách):** audit_sample_checked, ticket_reopened

---

## 3. Rủi ro kinh tế (lấy số từ bảng độ nhạy)

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
|--------|------------------|-------------------|-----------|-----------------|
| Số ca làm lại tăng gấp đôi | +51.8%, lên 6,787 đ [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4.9% trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11,743 đ = 0.98× (12,414 đ = 1.03× nếu làm lại 15.3 phút như dữ liệu) [simulated] | % yêu cầu được xem lại còn > 50% cuối bước 0.25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1,185 đ/việc ở 45,000 yc/tháng, +2,370 đ/việc nếu còn một nửa [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
| Mức chênh 6 điểm thay vì 5 điểm | Power giảm còn ~0.64 ở mức 5 điểm | Tỷ lệ phát hiện thấp hơn kỳ vọng | Tăng cỡ mẫu nếu có đủ nhân lực | Giám đốc vận hành |

### Ghi chú về rủi ro

- Xem lại 100% thì trợ lý gần như không tiết kiệm được gì (chi phí xem lại chiếm 90%).
- Mức hoà vốn: mỗi lần xem lại phải ≤ 5.1 phút (với 9 phút làm lại) hoặc ≤ 4.8 phút (với 15.3 phút).
- Nếu pilot có 20 người mỗi nhóm, tối đa 859 yêu cầu mỗi nhóm (20 × 299), chấp nhận mức chênh 6 điểm (power 0.64 ở mức 5 điểm).

---

## 4. Kết luận

- **Chỉ số chính trong đợt chạy thử là 82.83%**, cao hơn baseline 0.70.
- **Tỉ lệ bỏ qua gợi ý là 27.12%**, acceptable.
- **Tỉ lệ lỗi lọt đến khách là 4.25%**, acceptable.
- **Rủi ro chính là số ca làm lại và xem lại** - pilot phải theo dõi sát hai chỉ số này.
- **Chi phí mỗi việc thành công là 4,472 đ [simulated]**, bằng 0.37× so với nhân viên tự làm (12,000 đ).
