# 🤖 Trợ Lý Kỹ Sư AI & Hệ Thống Tiền Kiểm Bản Vẽ (Agentic Copilot & Intake)

## 1. Tầm nhìn thiết kế Trợ lý Kỹ sư (Agentic AI Copilot)

Khác với các chatbot giải đáp văn bản thông thường (Passive Chatbots), **Engenix Copilot** là một **Agentic AI Assistant** có năng lực thao tác trực tiếp với các dịch vụ lõi của ứng dụng (Application Core Services).

![Luồng tương tác của Copilot](../images/copilot_audit_flow.png)

---

## 2. Các Năng Lực Cốt Lõi (Key Capabilities)

### 2.1 Tiếp nhận tệp đa năng & Tiền kiểm (`KiemTraImport`)
- Người dùng có thể kéo thả đồng thời nhiều file với định dạng `.dwg`, `.dxf`, `.pdf` vector ngay trong khung chat.
- Hệ thống tự động phân loại cấu trúc hồ sơ bản vẽ và phát hiện **file còn thiếu**:
  - Có mặt bằng kiến trúc nhưng thiếu mặt bằng trần $\rightarrow$ Cảnh báo áp dụng chiều cao mặc định.
  - Có cửa trên tường nhưng thiếu bản vẽ định vị cửa $\rightarrow$ Thống kê bảng cảnh báo cho kỹ sư bổ sung hoặc cho phép bỏ qua để tiếp tục.

### 2.2 Modal thông tin dự án tích hợp
- Sau khi nhận file, Copilot hiển thị form tương tác điền thông tin:
  - Tên công trình / dự án.
  - Phân loại công trình (danh sách chuẩn: Nhà cao tầng, Nhà phố, Biệt thự,...).
  - Tên kỹ sư bóc tách (tự động lấy tên tài khoản đăng nhập nhưng cho phép điều chỉnh).

### 2.3 Khởi chạy bóc tách ngầm & Cập nhật tiến trình thời gian thực
- Sau khi người dùng nhấn **"Tiến hành bóc tách"**, Copilot gửi dữ liệu đến `/api/v1/process-drawings` và khởi tạo card tiến trình trực quan với 5 giai đoạn:
  1. ① Đọc cấu trúc & phân tách lớp CAD.
  2. ② Phân loại bản vẽ & cấu trúc tầng.
  3. ③ Phân loại lớp layer & block kết cấu.
  4. ④ Trích xuất ranh giới & đa giác khép kín.
  5. ⑤–⑩ Hoàn tất bóc tách & tính toán hình học.

### 2.4 Thẻ điều hướng kết quả thông minh (Deep Linking Cards)
Khi bóc tách hoàn tất 100%, Copilot hiển thị thẻ kết quả kèm các nút chuyển hướng trực tiếp:
- **3. Kiểm tra kết quả (CAD Viewport):** Mở bản vẽ CAD tương tác với vector các phòng vừa bóc tách.
- **4. Khối lượng & dự toán (Bóc tách):** Chuyển sang bảng soát xét chi tiết từng phòng.
- **5. Thống kê chi phí (Bảng giá sơn):** Xem tổng hợp dự toán và xuất file Excel.

---

## 3. Cơ Chế Audit Trail (Ghi Nhật Ký Kiểm Toán HITL)

Mọi hành động thao tác của Copilot đều tuân thủ chặt chẽ nguyên tắc **Human-in-the-Loop**:
- Mọi tác vụ tạo dự án, nạp bản vẽ, thay đổi đơn giá đều được ghi vào bảng `audit_events`.
- Đảm bảo tính minh bạch, truy xuất nguồn gốc (traceability) cho hồ sơ thanh quyết toán xây dựng.
