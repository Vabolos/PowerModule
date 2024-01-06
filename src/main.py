import tkinter
import tkinter.messagebox
import customtkinter
import sys

# components
from components.buttons.ClearConsoleButton import clear_console
from components.buttons.ConsoleInputButton import open_input_dialog_event
from components.buttons.CopyToBoardButton import copy_to_clipboard
from components.buttons.executeButton import sidebar_button_event_scriptExe
from components.buttons.discordButton import open_discord_server
from components.buttons.githubButton import open_github_repository
from components.buttons.openExplorerButton import open_explorer

# scripts
from components.scriptcalls.getAdGroupMember import getAdGroupMember
from components.scriptcalls.getGroupsMemberOf import getGroupsMemberOf
from components.scriptcalls.exportCsv import exportCSV
from components.scriptcalls.copyMemberOf import copyMemberOf
from components.scriptcalls.getPasswordStatus import getPasswordStatus


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("PowerModule Control Panel")
        self.geometry(f"{1100}x{580}")
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
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: open_github_repository(self), text="GitHub Repository")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: open_discord_server(self), text="Support Discord")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: clear_console(self))
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

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Search...")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(self.master, command=lambda: sidebar_button_event_scriptExe(self), text="Execute script")
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=450, state="disabled")
        self.textbox.grid(row=0, column=1, columnspan=2,  padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.tabview.add("Actions")
        self.tabview.tab("Actions").grid_columnconfigure(0, weight=1)

        self.clear_console_button = customtkinter.CTkButton(self.tabview.tab("Actions"), text="Clear console",
                                                            command=lambda: clear_console(self))
        self.clear_console_button.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.copy_to_clipboard_button = customtkinter.CTkButton(self.tabview.tab("Actions"), text="Copy to clipboard",
                                                                command=lambda: copy_to_clipboard(self))
        self.copy_to_clipboard_button.grid(row=0, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Actions"), text="Console Input Tester",
                                                           command=lambda: open_input_dialog_event(self))
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Actions"), text="Open file explorer", command=lambda: open_explorer(self))
        self.string_input_button.grid(row=5, column=0, padx=20, pady=(10, 10))
        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1) 

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Scripts")
        self.scrollable_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nwes")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        customtkinter.CTkButton(master=self.scrollable_frame, text="Get Members AD Group", command=lambda: getAdGroupMember(self)).grid(row=0, column=0, padx=20, pady=(5, 10))
        customtkinter.CTkButton(master=self.scrollable_frame, text="Get groups of member", command=lambda: getGroupsMemberOf(self)).grid(row=1, column=0, padx=20, pady=(10, 10))
        customtkinter.CTkButton(master=self.scrollable_frame, text="Copy user permissions", command=lambda: copyMemberOf(self)).grid(row=2, column=0, padx=20, pady=(10, 10))
        customtkinter.CTkButton(master=self.scrollable_frame, text="Export to CSV", command=lambda: exportCSV(self)).grid(row=3, column=0, padx=20, pady=(10, 10))
        customtkinter.CTkButton(master=self.scrollable_frame, text="Get Password Status", command=lambda: getPasswordStatus(self)).grid(row=4, column=0, padx=20, pady=(10, 10))

        # set default values
        self.sidebar_button_3.configure(state="disabled", text="Coming soon...")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox.configure(state="normal")
        self.textbox.insert("0.0", "Welcome to PowerModule!\n\n")
        self.textbox.configure(state="disabled")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()

    # close loop after closing window
    app.quit()