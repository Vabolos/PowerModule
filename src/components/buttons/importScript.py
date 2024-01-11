import tkinter as tk
from tkinter import filedialog, messagebox
from customtkinter import CTkTextbox

def import_script(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("PowerShell Script Files", "*.ps1")])

            if file_path and file_path.lower().endswith(".ps1"):
                with open(file_path, "r") as file:
                    script_content = file.read()

                    # Check if console_entry_widget is a CTkTextbox
                    if isinstance(self.textbox, CTkTextbox):
                        self.textbox.configure(state="normal")
                        self.textbox.insert(tk.END, "Script content: \n")
                        self.textbox.insert(tk.END, script_content + "\n")
                        self.textbox.focus()
                        self.textbox.see(tk.END)
                        self.textbox.update()
                        self.textbox.configure(state="disabled")
                    else:
                        messagebox.showerror("Error", "Invalid console entry widget.")
            elif file_path:
                messagebox.showerror("Error", "Only .ps1 files are supported!")
            else:
                messagebox.showinfo("Info", "No file selected.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"File not found: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file: {str(e)}")

def execute_script(self):
        try:
            script_content = self.textbox.get("1.0", tk.END)

            # Execute the script using subprocess and capture the output
            import subprocess
            result = subprocess.run(["powershell", "-Command", script_content], capture_output=True, text=True)

            # Insert the result into the CTkTextbox
            if isinstance(self.textbox, CTkTextbox):
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"Script Output:\n{result.stdout}\n")
                self.textbox.see(tk.END)
                self.textbox.update()
                self.textbox.configure(state="disabled")

            messagebox.showinfo("Info", "Script executed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error executing script: {str(e)}")
