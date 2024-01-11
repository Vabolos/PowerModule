import tkinter as tk
from tkinter import filedialog, messagebox

def import_script(self):
    file_path = filedialog.askopenfilename(filetypes=[("PowerShell Script Files", "*.ps1")])

    if file_path and file_path.lower().endswith(".ps1"):
        try:
            with open(file_path, "r") as f:
                data = f.read()
                self.consoleEntry.insert(tk.END, data + "\n")
                self.consoleEntry.focus()
                self.consoleEntry.see(tk.END)
                self.consoleEntry.update()
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file: {str(e)}")
    elif file_path:
        messagebox.showerror("Error", "Only .ps1 files are supported!")
        self.consoleEntry.focus()
        self.consoleEntry.see(tk.END)
        self.consoleEntry.update()