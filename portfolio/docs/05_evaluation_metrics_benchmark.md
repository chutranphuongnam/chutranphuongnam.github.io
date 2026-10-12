# 📊 Đánh Giá Hiệu Năng & Kết Quả Thực Nghiệm (Evaluation & Benchmarks)

## 1. Bảng Tổng Hợp 5 Dự Án Thực Nghiệm Gần Nhất (Top 5 Test Jobs)

Hệ thống ENGENIX đã được kiểm thử với các bộ hồ sơ bản vẽ thực tế (bao gồm tổ hợp chung cư cao tầng Tầng 15, Tầng 16, nhà phố, biệt thự và căn hộ mẫu):

![Tóm tắt đánh giá 5 Job gần nhất](../images/eval_jobs_summary.png)
![Chi tiết bảng khối lượng 5 Job](../images/eval_jobs_table.png)

---

## 2. Các Chỉ Số Hiệu Năng Trọng Yếu (Key Metrics)

| Chỉ số (Metric) | Bóc tách thủ công (Manual QS) | ENGENIX AI Platform | Mức độ cải thiện |
|---|---|---|---|
| **Thời gian bóc tách 1 tầng** | 3.5 – 6.0 giờ / tầng | **12 – 18 giây / tầng** | **Nhanh hơn 95%** 🚀 |
| **Độ chính xác nhận diện phòng** | 92% (phụ thuộc kinh nghiệm) | **96.8%** | Tự động hóa cao |
| **Sai số đo chu vi hình học** | ± 5% – 8% (đo tay thước CAD) | **< 2.1%** (Shapely Polygon) | Chuẩn xác theo vector |
| **Khấu trừ lỗ mở cửa & má cửa** | Dễ bỏ sót 15-20% cửa | **100% tự động trừ theo mã block** | Không bỏ sót |
| **Chi phí nhân sự / dự án** | 2.500.000 – 5.000.000 ₫ | **50.000 ₫ / lượt bóc tách** | **Tiết kiệm 98% chi phí** |

---

## 3. Phân Tích Chi Phí Token AI & Lợi Nhuận Biên

- **Mô hình AI sử dụng:** OpenAI `gpt-4o-mini`.
- **Đơn giá API:**
  - Input: $0.15 / 1M tokens.
  - Output: $0.60 / 1M tokens.
- **Tiêu thụ trung bình:** ~18.000 Input tokens và ~3.500 Output tokens cho một bộ hồ sơ tầng hoàn chỉnh $\approx$ **$0.005 USD (~130 VNĐ)**.
- **Giá bán dịch vụ:** 50.000 VNĐ / lượt quét bóc tách.
- **Biên lợi nhuận gộp:** **> 98%**, đảm bảo tính khả thi thương mại và mở rộng hạ tầng bền vững.
