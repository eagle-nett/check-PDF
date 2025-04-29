import os
import time
from datetime import datetime
from win32com.client import gencache

def open_and_save_copy_to_new_folder(src_folder, dst_folder, delay=1):
    # Tạo thư mục đích nếu chưa có
    os.makedirs(dst_folder, exist_ok=True)

    # Lấy danh sách tất cả file Excel trong thư mục
    files = [f for f in os.listdir(src_folder) if f.lower().endswith((".xls", ".xlsx"))]
    total_files = len(files)
    if total_files == 0:
        print("⚠️ Không tìm thấy file Excel nào trong thư mục.")
        return

    # Khởi tạo Excel COM an toàn
    excel = gencache.EnsureDispatch("Excel.Application")
    excel.Visible = False  # Ẩn cửa sổ Excel

    start_time = time.time()
    print(f"🚀 Tiến Đạt bắt đầu xử lý lúc: {datetime.now().strftime('%H:%M:%S')}")
    print(f"📦 Tổng số file cần xử lý: {total_files}\n")

    for index, filename in enumerate(files, start=1):
        src_path = os.path.join(src_folder, filename)

        # Thêm _copy vào tên file mới
        name, ext = os.path.splitext(filename)
        new_name = f"{name}_copy{ext}"
        dst_path = os.path.join(dst_folder, new_name)

        try:
            percent = (index / total_files) * 100
            print(f"[{index}/{total_files}] ({percent:.2f}%) 🔄 Đang xử lý: {filename}")

            workbook = excel.Workbooks.Open(src_path, UpdateLinks=0, ReadOnly=True)
            time.sleep(delay)
            workbook.SaveAs(dst_path)
            workbook.Close(False)

            print(f"✅ Đã lưu bản sao: {new_name}\n")
        except Exception as e:
            print(f"❌ Lỗi khi xử lý {filename}: {e}\n")

    excel.Quit()
    end_time = time.time()
    elapsed = end_time - start_time

    print("🎉 Xử lý hoàn tất!")
    print(f"📦 Tổng số file đã xử lý: {total_files}")
    print(f"⏱️ Thời gian thực hiện: {elapsed:.2f} giây ({elapsed/60:.2f} phút)")

# --- Cấu hình ---
source_folder = r"E:\checkEX"        # Thư mục chứa file gốc
destination_folder = r"E:\helpEX"     # Thư mục chứa bản sao

# --- Chạy ---
open_and_save_copy_to_new_folder(source_folder, destination_folder)
