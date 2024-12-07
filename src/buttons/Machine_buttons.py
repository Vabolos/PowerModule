import customtkinter
from customImporting import *

def create_machine_buttons(scrollable_frame):
    machine_buttons = [
        customtkinter.CTkButton(master=scrollable_frame, text="Change Name", command=lambda: name_change_machine()).grid(row=0, column=0, padx=20, pady=(10, 5)),
        customtkinter.CTkButton(master=scrollable_frame, text="Add to Domain", command=lambda: add_to_domain_machine()).grid(row=1, column=0, padx=20, pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Release/Renew IP", command=lambda: ip_release_renew()).grid(row=2, column=0, padx=20, pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Disk Cleaner", command=lambda: disk_cleaner_machine()).grid(row=3, column=0, padx=20, pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Get Battery Report", command=lambda: battery_report()).grid(row=4, column=0, padx=20, pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Flush DNS", command=lambda: flush_dns_machine()).grid(row=5, column=0, padx=20, pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Clear Temp Files", command=lambda: clear_temp_files()).grid(row=6, column=0, padx=20, pady=5)
    ]
    return machine_buttons