# BN10 SCRAPER - Bot Tra Điểm Tuyển Sinh Lớp 10 Bắc Ninh

BN10 Scraper là một công cụ mã nguồn mở được phát triển nhằm hỗ trợ việc tự động hóa thu thập và thống kê số liệu điểm thi tuyển sinh vào lớp 10 THPT tại tỉnh Bắc Ninh phục vụ mục đích nghiên cứu và phân tích dữ liệu giáo dục.

⚠️ **TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM (IMPORTANT DISCLAIMER)**
* **Mục đích duy nhất:** Công cụ này được viết ra hoàn toàn vì mục đích học tập, nghiên cứu khoa học dữ liệu (Data Science) và phân tích thống kê cá nhân. Tác giả không khuyến khích, không cổ xúy và không chịu trách nhiệm cho bất kỳ hành vi sử dụng dữ liệu sai mục đích nào.
* **Bảo vệ dữ liệu cá nhân:** Dữ liệu điểm thi chứa thông tin cá nhân của học sinh (Họ tên, SBD, Trường, Điểm số). Việc lưu trữ bừa bãi hoặc tự ý phát tán, công khai danh sách này lên các nền tảng mạng xã hội hoặc xây dựng website tra cứu thương mại mà chưa có sự đồng ý của cơ quan quản lý có thể vi phạm pháp luật hiện hành về Bảo vệ dữ liệu cá nhân (Nghị định 13/2023/NĐ-CP).
* **Trách nhiệm vận hành:** Người sử dụng tự chịu hoàn toàn trách nhiệm trước pháp luật nếu hành vi cào dữ liệu của mình làm gián đoạn, quá tải hoặc gây ảnh hưởng tiêu cực đến hệ thống máy chủ của Sở GD&ĐT Bắc Ninh.

---

## 🚀 Tính năng nổi bật
* Tự động hóa quá trình gửi request tra cứu theo dải số báo danh (SBD).
* Trích xuất dữ liệu trả về và cấu trúc hóa thành định dạng sạch (`.csv` hoặc `.json`).
* Tích hợp cơ chế **Rate Limiting** (giới hạn tốc độ) thông minh để bảo vệ hạ tầng máy chủ đích.
