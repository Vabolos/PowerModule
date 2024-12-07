import customtkinter
from customImporting import *

def create_adm_buttons(scrollable_frame):
    adm_buttons = [
        customtkinter.CTkButton(master=scrollable_frame, text="Get Members AD Group", command=lambda: get_ad_group_member_server()).pack(pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Get Groups Member Of", command=lambda: get_group_member_of_server()).pack(pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Export CSV", command=lambda: export_csv_server()).pack(pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Copy Member Of", command=lambda: copy_member_of_server()).pack(pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Get Password Status", command=lambda: get_password_status_server()).pack(pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="List Disabled Users", command=lambda: list_disabled_users_server()).pack(pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="List Locked Users", command=lambda: list_lockedout_users_server()).pack(pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Flush DNS", command=lambda: flush_dns_server()).pack(pady=5),
        customtkinter.CTkButton(master=scrollable_frame, text="Unlock Locked Users", command=lambda: unlock_locked_users()).pack(pady=5)
    ]
    return adm_buttons