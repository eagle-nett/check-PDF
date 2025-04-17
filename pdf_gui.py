import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PyPDF2 import PdfReader

def check_pdfs(folder_path):
    ok_files = []
    corrupted_files = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            try:
                reader = PdfReader(file_path)
                _ = len(reader.pages)
                ok_files.append(filename)
            except Exception as e:
                corrupted_files.append((filename, str(e)))

    return ok_files, corrupted_files

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_selected)

def run_check():
    folder = folder_entry.get()
    if not os.path.exists(folder):
        messagebox.showerror("Lỗi", "Thư mục không tồn tại.")
        return

    ok_files, corrupted_files = check_pdfs(folder)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "✅ File hợp lệ:\n")
    for f in ok_files:
        result_text.insert(tk.END, f"  - {f}\n")

    result_text.insert(tk.END, "\n❌ File lỗi:\n")
    for f, err in corrupted_files:
        result_text.insert(tk.END, f"  - {f} → {err}\n")

def export_log():
    log_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv")])
    if not log_path:
        return
    try:
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(result_text.get(1.0, tk.END))
        messagebox.showinfo("Thành công", f"Đã lưu kết quả vào:\n{log_path}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# GUI
root = tk.Tk()
root.title("🔍 PDF Checker Tool")
root.geometry("700x500")

tk.Label(root, text="📁 Chọn thư mục chứa PDF:").pack(pady=5)
frame = tk.Frame(root)
frame.pack()

folder_entry = tk.Entry(frame, width=60)
folder_entry.pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Duyệt...", command=browse_folder).pack(side=tk.LEFT)

tk.Button(root, text="🚀 Kiểm tra PDF", command=run_check, bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)

result_text = scrolledtext.ScrolledText(root, width=85, height=20)
result_text.pack(padx=10, pady=5)

tk.Button(root, text="💾 Xuất kết quả", command=export_log).pack(pady=10)

root.mainloop()
