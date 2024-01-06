import customtkinter

def open_input_dialog_event(self):
    dialog = customtkinter.CTkInputDialog(text="Type in test text:", title="Console tester")
    print("[Console]", dialog.get_input())