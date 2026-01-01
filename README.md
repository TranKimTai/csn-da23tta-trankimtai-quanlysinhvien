# Thiết kế và Cài đặt CSDL NoSQL Quản lý Sinh viên

Dự án nghiên cứu và triển khai hệ thống quản lý sinh viên dựa trên nền tảng **MongoDB**, tập trung vào việc tối ưu hóa hiệu năng truy xuất và xử lý dữ liệu phi cấu trúc thông qua kỹ thuật nhúng (Embedding) và Aggregation.

## 📖 Giới thiệu

Dự án được thực hiện nhằm giải quyết các hạn chế của SQL truyền thống trong việc quản lý dữ liệu giáo dục. Hệ thống cho phép:

* Lưu trữ hồ sơ sinh viên đa cấp (Lớp, Khoa, Cố vấn học tập).
* Truy xuất dữ liệu tốc độ cao không cần phép JOIN.
* Báo cáo thống kê thời gian thực dựa trên các tiêu chí phức tạp.

## 🏗 Cấu trúc dữ liệu

Dự án áp dụng mô hình **Document-based** với chiến lược **Embedding** giúp dữ liệu luôn nhất quán và dễ mở rộng.

**Các trường dữ liệu chính:**

* `ma_sinh_vien`: Mã số sinh viên (Unique Key).
* `thong_tin_lop`: Chứa dữ liệu nhúng về lớp học và Cố vấn học tập.
* `thong_tin_khoa`: Chứa dữ liệu nhúng về khoa quản lý.
* `dia_chi`: Thông tin thường trú/tạm trú.

## 🛠 Cài đặt

1. **Yêu cầu hệ thống:**
* Cài đặt [MongoDB Community Server v6.0+](https://www.mongodb.com/try/download/community).
* Cài đặt [MongoDB Compass](https://www.mongodb.com/try/download/compass).

2. **Khởi tạo dữ liệu:**
Mở terminal hoặc MongoDB Shell và thực thi lệnh sau:
```javascript
use quan_ly_sinh_vien
db.createCollection("sinh_vien")

```

## 💻 Cách sử dụng

### Truy xuất thông tin chi tiết

Dùng để lấy toàn bộ thông tin sinh viên bao gồm cả thông tin lớp/khoa:

```javascript
db.sinh_vien.findOne({ "ma_sinh_vien": "110123042" })

```

### Thống kê sĩ số theo giới tính và khoa

Sử dụng Aggregation Pipeline để xuất báo cáo:

```javascript
db.sinh_vien.aggregate([
  { $group: {
      _id: "$thong_tin_khoa.ten_khoa",
      sv_nam: { $sum: { $cond: [{ $eq: ["$gioi_tinh", "Nam"] }, 1, 0] } },
      sv_nu: { $sum: { $cond: [{ $eq: ["$gioi_tinh", "Nữ"] }, 1, 0] } }
  }}
])

```

## ✅ Đánh giá kết quả

* **Hiệu năng:** Tốc độ phản hồi truy vấn đạt mức tối ưu (<1ms) nhờ lược đồ nhúng dữ liệu.
* **Linh hoạt:** Dễ dàng bổ sung các trường thông tin mới (như chứng chỉ, kỹ năng) cho từng sinh viên mà không cần sửa cấu trúc toàn bộ bảng.
* **Trực quan:** Xây dựng thành công Dashboard quản trị trên MongoDB Compass giúp theo dõi sĩ số và phân bố địa lý sinh viên.

---
**Người thực hiện:** Trần Kim Tài
**Email:** kimtaitran278@gmail.com
