# Thiết kế và Cài đặt Cơ sở Dữ liệu NoSQL cho Hệ thống Quản lý Sinh viên

Dự án này tập trung vào việc nghiên cứu, thiết kế và triển khai một hệ thống quản lý sinh viên sử dụng cơ sở dữ liệu phi quan hệ (NoSQL) với **MongoDB**. Mục tiêu chính là tối ưu hóa hiệu suất truy xuất dữ liệu và đảm bảo tính linh hoạt trong quản lý hồ sơ sinh viên tại môi trường đại học.

## 📌 Tổng quan dự án
[cite_start]Dự án giải quyết bài toán quản lý sinh viên thông qua các kỹ thuật hiện đại của MongoDB, thay thế cho các phương pháp SQL truyền thống để tăng tốc độ xử lý các truy vấn phức tạp và báo cáo thống kê.

## 🛠 Công nghệ sử dụng
* [cite_start]**Hệ quản trị CSDL:** MongoDB Community Server (v6.0).
* [cite_start]**Công cụ quản lý:** MongoDB Compass (Giao diện đồ họa) và MongoDB Shell (Dòng lệnh).
* [cite_start]**Kiến trúc dữ liệu:** Document-based với định dạng BSON/JSON.

## 📂 Cấu trúc Chương trong báo cáo
1. **Chương 1: Tổng quan về đề tài:** Lý do chọn đề tài và mục tiêu nghiên cứu.
2. [cite_start]**Chương 2: Cơ sở lý thuyết:** Giới thiệu về NoSQL, MongoDB và các khái niệm Document, Collection.
3. [cite_start]**Chương 3: Hiện thực hóa nghiên cứu:** Thiết kế ERD, lược đồ mức vật lý và cài đặt hệ thống.
4. [cite_start]**Chương 4: Kết quả và Thảo luận:** Thực thi các nghiệp vụ cập nhật, tra cứu và Dashboard thống kê.

## 🏗 Đặc điểm kỹ thuật nổi bật
* [cite_start]**Chiến lược Embedding (Nhúng):** Nhúng trực tiếp thông tin Lớp, Khoa và Cố vấn học tập vào Document Sinh viên để loại bỏ các phép `JOIN` tốn kém tài nguyên.
* [cite_start]**Aggregation Pipeline:** Sử dụng các đường ống xử lý dữ liệu để tạo ra các báo cáo thống kê về sĩ số theo khoa, giới tính và phân bố địa lý một cách nhanh chóng.
* [cite_start]**Tính linh hoạt cao:** Cho phép thay đổi cấu trúc dữ liệu (như thêm chứng chỉ, thông tin phụ) cho từng nhóm sinh viên mà không cần thay đổi lược đồ toàn bộ hệ thống.

## 📊 Các nghiệp vụ đã thực hiện
* [cite_start]**Cập nhật:** Hỗ trợ cập nhật hồ sơ cá nhân và cập nhật hàng loạt (ví dụ: cập nhật học kỳ cho cả lớp).
* [cite_start]**Tra cứu:** Tìm kiếm chính xác theo mã sinh viên và tìm kiếm linh hoạt bằng biểu thức chính quy (Regex) theo địa chỉ, tên.
* [cite_start]**Thống kê:** Tự động tổng hợp số liệu sinh viên theo từng khoa và tỉnh thành thông qua toán tử `$group` và `$merge`.

## 🚀 Cài đặt
1. Cài đặt MongoDB Server và MongoDB Compass.
2. Khởi tạo database `quan_ly_sinh_vien`.
3. Import dữ liệu mẫu từ file JSON đính kèm (nếu có).
4. Thực thi các truy vấn mẫu trong thư mục `queries/`.

---
[cite_start]**Tác giả:** Trần Kim Tài 
[cite_start]**Giảng viên hướng dẫn:** Phan Thị Phương Nam
