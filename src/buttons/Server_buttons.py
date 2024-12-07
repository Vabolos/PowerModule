import customtkinter
from customImporting import *

def create_server_buttons(scrollable_frame):
    server_buttons = [
        customtkinter.CTkButton(master=scrollable_frame, text="Change Name", command=lambda: name_change_server()).grid(row=0, column=0, padx=20, pady=(10, 5)),
        customtkinter.CTkButton(master=scrollable_frame, text="Add to Domain", command=lambda: add_to_domain_server()).grid(row=1, column=0, padx=20, pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Setup IPv4", command=lambda: setup_IPv4()).grid(row=2, column=0, padx=20, pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Disk Cleaner", command=lambda: disk_cleaner_server()).grid(row=3, column=0, padx=20, pady=5)
    ]
    return server_buttons