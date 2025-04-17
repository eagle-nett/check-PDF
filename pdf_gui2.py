import os
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox
from PyPDF2 import PdfReader

def check_pdf_valid(filepath):
    try:
        reader = PdfReader(filepath)
        _ = reader.pages[0]  # Thử truy cập trang đầu tiên
        return True
    except:
        return False

def browse_folder():
    folder = filedialog.askdirectory()
    if not folder:
        return
    entry_folder.delete(0, tk.END)
    entry_folder.insert(0, folder)
    listbox.delete(0, tk.END)

    for file in os.listdir(folder):
        if file.lower().endswith(".pdf"):
            path = os.path.join(folder, file)
            if not check_pdf_valid(path):
                listbox.insert(tk.END, file)

def open_with_notepad():
    selected = listbox.curselection()
    if selected:
        file = listbox.get(selected[0])
        full_path = os.path.join(entry_folder.get(), file)
        os.system(f'notepad "{full_path}"')

def open_with_default():
    selected = listbox.curselection()
    if selected:
        file = listbox.get(selected[0])
        full_path = os.path.join(entry_folder.get(), file)
        os.startfile(full_path)

# GUI setup
root = tk.Tk()
root.title("PDF Lỗi Checker")

tk.Label(root, text="Chọn thư mục chứa PDF:").pack(pady=5)

entry_folder = tk.Entry(root, width=50)
entry_folder.pack(padx=10)

tk.Button(root, text="📁 Duyệt thư mục", command=browse_folder).pack(pady=5)

listbox = Listbox(root, width=60, height=15)
listbox.pack(padx=10, pady=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack()

tk.Button(frame_buttons, text="📝 Mở bằng Notepad", command=open_with_notepad).pack(side=tk.LEFT, padx=10)
tk.Button(frame_buttons, text="📂 Mở bằng app mặc định", command=open_with_default).pack(side=tk.LEFT, padx=10)

root.mainloop()
