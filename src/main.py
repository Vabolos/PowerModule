import tkinter
import tkinter.messagebox
import customtkinter
import sys

from customImporting import *

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("PowerModule Control Panel")
        self.geometry(f"{1200}x{680}")
        self.resizable(False, False)

        # configure window icon
        self.iconbitmap("powermodule.ico")

        # configure grid layout (3x3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # redirect vsc terminal output to textbox
        def redirector(input_str):
            self.textbox.configure(state="normal")
            self.textbox.insert("end", input_str)
            self.textbox.configure(state="disabled")
        sys.stdout.write = redirector

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Power Module", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, 
                                                        command=lambda: open_github_repository(self), text="GitHub Repository")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, 
                                                        command=lambda: open_discord_server(self), text="Support Discord")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, 
                                                        command=lambda: import_script(self), text="Import script")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # input field
        self.entry = customtkinter.CTkEntry(self, placeholder_text="> _", width=30)
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        app_functions = AppFunctions(self)  # Pass the instance of App to AppFunctions
        self.entry.bind("<Return>", lambda event: app_functions.execute_command(event))
        self.functions = app_functions  # Assign the functions instance to the App class
        self.process = None

        self.main_button_1 = customtkinter.CTkButton(self.master, 
                                                     command=lambda: execute_script(self), text="Execute script")
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # console
        self.textbox = customtkinter.CTkTextbox(self, width=450, state="disabled", font=customtkinter.CTkFont(size=15, weight="bold", family="Consolas"))
        self.textbox.grid(row=0, rowspan=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create script tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=1, column=3, padx=(20, 20), pady=(10, 0), sticky="nsew")

        # Adding "Machine" tab
        self.tabview.add("Machine")
        self.tabview.tab("Machine").grid_columnconfigure(0, weight=1)

        # create scrollable frame for the "Machine" tab
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab("Machine"))
        self.scrollable_frame.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)

        # Adding "Machine" buttons
        customtkinter.CTkButton(master=self.scrollable_frame, text="Change Name",
                                command=lambda: name_change_machine(self)).grid(row=0, column=0, padx=20, pady=(10, 5))
        customtkinter.CTkButton(master=self.scrollable_frame, text="Add to Domain",
                                command=lambda: add_to_domain_machine(self)).grid(row=1, column=0, padx=20, pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Release/Renew IP",
                                command=lambda: ip_release_renew(self)).grid(row=2, column=0, padx=20, pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Disk Cleaner",
                                command=lambda: disk_cleaner_machine(self)).grid(row=3, column=0, padx=20, pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Get Battery Report",
                                command=lambda: battery_report(self)).grid(row=4, column=0, padx=20, pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Flush DNS",
                                command=lambda: flush_dns_machine(self)).grid(row=4, column=0, padx=20, pady=5)

        # Adding "Server" tab
        self.tabview.add("Server")
        self.tabview.tab("Server").grid_columnconfigure(0, weight=1)

        # create scrollable frame for the "Server" tab
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab("Server"))
        self.scrollable_frame.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)

        # Adding "Server" buttons
        customtkinter.CTkButton(master=self.scrollable_frame, text="Change Name",
                                command=lambda: name_change_server(self)).grid(row=0, column=0, padx=20, pady=(10, 5))
        customtkinter.CTkButton(master=self.scrollable_frame, text="Add to Domain",
                                command=lambda: add_to_domain_server(self)).grid(row=1, column=0, padx=20, pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Setup IPv4",
                                command=lambda: setup_IPv4(self)).grid(row=2, column=0, padx=20, pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Disk Cleaner",
                                command=lambda: disk_cleaner_server()).grid(row=3, column=0, padx=20, pady=5)
        
        # Update the geometry of the frame to make it expand with the window
        self.tabview.tab("Server").update_idletasks()
        self.scrollable_frame.config(width=self.tabview.tab("Server").winfo_width(), height=self.tabview.tab("Server").winfo_height())

        # Adding existing "Active Directory Manager" tab
        self.tabview.add("ADM")
        self.tabview.tab("ADM").grid_columnconfigure(0, weight=1)

        # Creating a scrollable frame for the "Active Directory Manager" tab
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab("ADM"))
        self.scrollable_frame.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)

        # Script buttons (Active Directory Manager)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Get Members AD Group",
                                command=lambda: get_ad_group_member_server(self)).pack(pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Get Groups Member Of",
                                command=lambda: get_group_member_of_server(self)).pack(pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Export CSV",
                                command=lambda: export_csv_server(self)).pack(pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Copy Member Of",
                                command=lambda: copy_member_of_server(self)).pack(pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Get Password Status",
                                command=lambda: get_password_status_server(self)).pack(pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="List Disabled Users",
                                command=lambda: list_disabled_users_server(self)).pack(pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="List Locked Users",
                                command=lambda: list_lockedout_users_server(self)).pack(pady=5)
        customtkinter.CTkButton(master=self.scrollable_frame, text="Flush DNS",
                                command=lambda: flush_dns_server(self)).pack(pady=5)

        # Update the geometry of the frame to make it expand with the window
        self.tabview.tab("ADM").update_idletasks()
        self.scrollable_frame.config(width=self.tabview.tab("ADM").winfo_width(), height=self.tabview.tab("ADM").winfo_height())

        # create actions tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=2, column=3, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self.tabview.add("Actions")
        self.tabview.tab("Actions").grid_columnconfigure(0, weight=1)
        

        # Action buttons
        customtkinter.CTkButton(master=self.tabview.tab("Actions"), text="Clear console", 
                                command=lambda: clear_console(self)).grid(row=1, column=0, padx=20, pady=(5, 10))
        customtkinter.CTkButton(master=self.tabview.tab("Actions"), text="Copy to clipboard", 
                                command=lambda: copy_to_clipboard(self)).grid(row=0, column=0, padx=20, pady=(5, 10))
        customtkinter.CTkButton(master=self.tabview.tab("Actions"), text="Console Input Tester", 
                                command=lambda: open_input_dialog_event(self)).grid(row=2, column=0, padx=20, pady=(5, 10))
        customtkinter.CTkButton(master=self.tabview.tab("Actions"), text="Restart machine", 
                                command=lambda: restart_machine(self)).grid(row=3, column=0, padx=20, pady=(5, 10))
        customtkinter.CTkButton(master=self.tabview.tab("Actions"), text="Open notepad",
                                command=lambda: open_notepad(self)).grid(row=4, column=0, padx=20, pady=(5, 10))
        customtkinter.CTkButton(master=self.tabview.tab("Actions"), text="Open powershell",
                                command=lambda: open_powershell()).grid(row=5, column=0, padx=20, pady=(5, 10))

        # default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox.configure(state="normal")
        self.textbox.insert("0.0", "Welcome to PowerModule!\n\nType 'powershell' to open a PowerShell console, and 'exit' to close it.\n\n")
        self.textbox.configure(state="disabled")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()
    app.quit()