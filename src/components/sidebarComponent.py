 # create sidebar frame with widgets
import customtkinter
import tkinter
import tkinter.messagebox
import webbrowser
import sys

class Sidebar:
    def __init__(self, parent):

        # redirect vsc terminal output to textbox
        def redirector(input_str):
            self.textbox.configure(state="normal")
            self.textbox.insert("end", input_str)
            self.textbox.configure(state="disabled")

        sys.stdout.write = redirector
        sys.stderr.write = redirector

        # create textbox
        self.textbox = customtkinter.CTkTextbox(
            self, width=250, state="disabled")
        self.textbox.grid(row=0, column=1, padx=(
            20, 0), pady=(20, 0), sticky="nsew")

        # create sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(parent, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Power Module", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_github_repository, text="GitHub Repository")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_discord_server, text="Support Discord")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
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

        self.textbox.configure(state="normal")
        self.textbox.configure(state="disabled")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")
        self.textbox.configure(state="disabled")

    def sidebar_button_event_scriptExe(self):
        tkinter.messagebox.showinfo("Info", "This feature is not implemented yet.")
        print("unimplemented feature was called")

    def open_github_repository(self):
        url: str = "https://github.com/Vabolos/PowerModule"
        webbrowser.open(url)
        print("Opened GitHub repository in browser.")

    def open_discord_server(self):
        url: str = "https://discord.gg/HuP3gjrRzb"
        webbrowser.open(url)
        print("Opened Discord server in browser or app.")