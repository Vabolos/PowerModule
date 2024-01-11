import subprocess
from tkinter import messagebox

def restart_machine(self):
    try:
        # Display confirmation dialog
        user_response = messagebox.askyesno("Confirmation", "Are you sure you want to restart the machine?", parent=self)

        # Check user response
        if user_response:
            result = subprocess.run(["shutdown", "/r", "/t", "0"], capture_output=True, text=True)

            if result.returncode == 0:
                messagebox.showinfo("Info", "Machine is restarting...")
            else:
                messagebox.showerror("Error", f"Error restarting machine: {result.stderr}")
        else:
            messagebox.showinfo("Info", "Restart canceled.")
    except Exception as e:
        messagebox.showerror("Error", f"Error restarting machine: {str(e)}")
