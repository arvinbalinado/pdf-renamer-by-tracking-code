import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from renamer import rename_pdfs_in_folder

class PDFRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Renamer by Tracking Code")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.selected_folder = ""
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Step 1: Select Folder Containing PDFs", font=("Arial", 12)).pack(pady=10)

        browse_btn = tk.Button(self.root, text="📂 Browse Folder", command=self.select_folder, width=25)
        browse_btn.pack()

        self.folder_label = tk.Label(self.root, text="No folder selected", fg="gray")
        self.folder_label.pack(pady=5)

        tk.Label(self.root, text="Step 2: Click Rename", font=("Arial", 12)).pack(pady=10)

        rename_btn = tk.Button(self.root, text="🚀 Start Renaming", command=self.rename_files, bg="green", fg="white", width=25)
        rename_btn.pack(pady=5)

        self.log_area = scrolledtext.ScrolledText(self.root, width=70, height=10)
        self.log_area.pack(pady=10)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder = folder
            self.folder_label.config(text=folder, fg="black")

    def rename_files(self):
        if not self.selected_folder:
            messagebox.showwarning("Folder Missing", "Please select a folder containing PDF files.")
            return

        self.log_area.delete(1.0, tk.END)
        self.log_area.insert(tk.END, f"Renaming started for folder:\n{self.selected_folder}\n\n")

        try:
            renamed_count = rename_pdfs_in_folder(self.selected_folder, self.log_area)
            self.log_area.insert(tk.END, f"\n✅ Done! {renamed_count} file(s) renamed.\n")
        except Exception as e:
            self.log_area.insert(tk.END, f"\n❌ Error: {str(e)}\n")
            messagebox.showerror("Renaming Failed", f"An error occurred:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFRenamerApp(root)
    root.mainloop()
