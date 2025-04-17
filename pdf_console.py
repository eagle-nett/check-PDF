import os
from PyPDF2 import PdfReader

# Thư mục chứa các file PDF
folder_path = r"C:\tdat\CODE\check pdf\pdf test"

# Kết quả
ok_files = []
corrupted_files = []

# Duyệt tất cả file trong thư mục
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".pdf"):
        file_path = os.path.join(folder_path, filename)
        try:
            reader = PdfReader(file_path)
            # Gọi 1 lần để trigger lỗi nếu có
            _ = len(reader.pages)
            ok_files.append(filename)
        except Exception as e:
            corrupted_files.append((filename, str(e)))

# In kết quả
print("\n📄 KẾT QUẢ KIỂM TRA PDF\n")

print("✅ File hợp lệ:")
for f in ok_files:
    print("  -", f)

print("\n❌ File hỏng:")
for f, err in corrupted_files:
    print(f"  - {f} → Lỗi: {err}")
