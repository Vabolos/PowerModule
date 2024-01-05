 # create sidebar frame with widgets
import customtkinter
import tkinter
import tkinter.messagebox
import webbrowser

def clear_console(self):
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

def copy_to_clipboard(self):
    self.clipboard_clear()
    self.clipboard_append(self.textbox.get("0.0", "end"))
    print("Copied text to clipboard.")

def open_input_dialog_event(self):
    dialog = customtkinter.CTkInputDialog(text="Type in test text:", title="Console tester")
    print("[Console]", dialog.get_input())

def clear_console_button_event(self):
    self.textbox.configure(state="normal")
    self.textbox.delete("0.0", "end")
    self.textbox.configure(state="disabled")
    print("Cleared console.")