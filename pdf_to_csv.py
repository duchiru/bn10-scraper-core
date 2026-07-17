import pdfplumber
import pandas as pd
import os
import gc

def pdf_to_csv(pdf_path, csv_path):
    print("Đang xử lý file PDF...")
    
    # Định nghĩa chính xác tên các cột dựa theo cấu trúc bảng điểm trong ảnh của bạn
    columns = [
        "TT", "Số báo danh", "Họ và tên", "Giới tính", "Ngày sinh", 
        "Điểm ưu tiên", "Điểm Khuyến khích", "Ngữ Văn", "Điểm Tiếng Anh", 
        "Toán Trắc Nghiệm", "Toán Tự Luận", "Tổng toán", "Tổng đại trà", 
        "Môn Chuyên", "Điểm chuyên", "Tên trường"
    ]

    # Xóa file CSV cũ nếu đã tồn tại để tránh ghi đè/nối vào dữ liệu cũ
    if os.path.exists(csv_path):
        os.remove(csv_path)
        
    found_data = False
    
    # Mở file PDF
    with pdfplumber.open(pdf_path) as pdf:
        # Duyệt qua từng trang của file PDF
        for i, page in enumerate(pdf.pages):
            print(f"Đang trích xuất và lưu trang {i + 1}...")
            
            # Trích xuất bảng từ trang
            table = page.extract_table()
            
            if table:
                found_data = True
                
                # Nếu không phải trang đầu tiên, bỏ dòng tiêu đề (dòng đầu tiên) nếu có
                if i > 0:
                    table = table[1:]
                    
                if not table:
                    continue

                # Chuyển đổi thành DataFrame để xử lý dữ liệu
                df = pd.DataFrame(table)
                
                # Kiểm tra số lượng cột trích xuất được để gán tên cho phù hợp
                if df.shape[1] == len(columns):
                    df.columns = columns
                    # Loại bỏ các dòng tiêu đề nếu bị lặp lại trong dữ liệu
                    df = df[df["TT"] != "TT"]
                else:
                    if i == 0:
                        print(f"Lưu ý: Số lượng cột trích xuất thực tế ({df.shape[1]}) khác với số lượng cột dự kiến ({len(columns)}).")
                    # Nếu lệch cột, tự động đánh tên cột mặc định
                    df.columns = [f"Col_{idx}" for idx in range(df.shape[1])]
                
                # Xóa các dòng trống hoàn toàn (nếu có)
                df.dropna(how='all', inplace=True)
                
                if df.empty:
                    continue
                
                # Lưu dữ liệu ra file CSV theo từng trang. Dùng mode='a' để nối tiếp.
                # Ghi tiêu đề (header) nếu file chưa tồn tại
                write_header = not os.path.exists(csv_path)
                df.to_csv(csv_path, mode='a', index=False, header=write_header, encoding='utf-8-sig')
            
            # ---- GIẢI PHÓNG BỘ NHỚ SAU KHI XONG MỖI TRANG ----
            page.flush_cache()
            if 'table' in locals():
                del table
            if 'df' in locals():
                del df
            gc.collect()
                    
    if not found_data:
        print("Không tìm thấy bảng dữ liệu nào trong file PDF.")
        return

    print(f"Chuyển đổi thành công! File CSV đã được lưu tại: {csv_path}")

# --- CẤU HÌNH ĐƯỜNG DẪN FILE TẠI ĐÂY ---
pdf_file_path = "result.pdf"
csv_file_path = "result.csv"

# Chạy hàm chuyển đổi
if __name__ == "__main__":
    pdf_to_csv(pdf_file_path, csv_file_path)