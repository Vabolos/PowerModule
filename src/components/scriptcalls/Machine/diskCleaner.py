import tkinter as tk
from tkinter import ttk

class DiskCleanupApp:
    def __init__(self, root, disk_cleaner_function):
        self.root = root
        self.root.title("Disk Cleanup Options")
        self.disk_cleaner_function = disk_cleaner_function

        self.checkboxes = {
            "Temporary Files": tk.BooleanVar(),
            "Recycle Bin": tk.BooleanVar(),
            "System created Windows Error Reporting": tk.BooleanVar(),
            # Add more checkboxes as needed
        }

        self.create_gui()

    def create_gui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0)

        ttk.Label(main_frame, text="Select items to clean up:").grid(row=0, column=0, columnspan=2, pady=(0, 10))

        row_num = 1
        for label, var in self.checkboxes.items():
            ttk.Checkbutton(main_frame, text=label, variable=var).grid(row=row_num, column=0, sticky="w")
            row_num += 1

        ttk.Button(main_frame, text="Clean Up", command=self.clean_up).grid(row=row_num, column=0, columnspan=2, pady=(10, 0))

    def clean_up(self):
        selected_options = [label for label, var in self.checkboxes.items() if var.get()]
        print("Cleaning up selected options:", selected_options)
        # Call the provided disk cleaner function with selected options
        self.disk_cleaner_function(selected_options)

def disk_cleaner_machine(selected_options):
    # Implement your disk cleanup logic here based on the selected options
    print("Performing disk cleanup with options:", selected_options)
    # Add your cleanup logic for each selected option
    if "Temporary Files" in selected_options:
        print("Cleaning up Temporary Files...")