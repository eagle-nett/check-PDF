import filetype
import PyPDF2

file_path = r"C:\tdat\CODE\check pdf\pdf test\(34266).pdf"  

# Mở file và đọc vào buffer
with open(file_path, 'rb') as f:
    kind = filetype.guess(f)

if kind:
    print(f"📄 File này thực ra là: {kind.mime} ({kind.extension})")
else:
    print("❓ Không xác định được loại file – có thể rỗng hoặc quá hỏng.")


try:
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        if reader.pages:
            print(f"✅ File PDF hợp lệ với {len(reader.pages)} trang.")
        else:
            print("❓ File PDF không có trang hoặc bị hỏng.")
except Exception as e:
    print(f"❌ Lỗi khi mở file PDF: {e}")