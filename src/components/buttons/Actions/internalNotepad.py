import customtkinter
import tkinter.messagebox
import os

def save_text_locally(textbox):
    text_to_save = textbox.get("1.0", "end-1c")  # Get text from the textbox
    with open("saved_text.txt", "w") as file:
        file.write(text_to_save)
    return

def load_saved_text(textbox):
    try:
        with open("saved_text.txt", "r") as file:
            saved_text = file.read()
            textbox.insert("1.0", saved_text)  # Insert the saved text into the textbox
    except FileNotFoundError:
        return

def clear_notepad(textbox):
    textbox.delete("1.0", "end")  # Clear all content from the textbox

def open_notepad(self):
    notepad = customtkinter.CTk()
    notepad.title("Notepad")
    notepad.geometry(f"{800}x{600}")
    notepad.resizable(False, False)
    notepad.iconbitmap("powermodule.ico")

    textbox = customtkinter.CTkTextbox(notepad, width=750, height=500)
    textbox.grid(row=0, column=0, padx=20, pady=20)
    textbox.grid_rowconfigure(0, weight=1)
    textbox.grid_columnconfigure(0, weight=1)

    load_saved_text(textbox)

    def on_close():
        save_text_locally(textbox)
        notepad.destroy()

    # Clear Notepad button
    clear_button = customtkinter.CTkButton(notepad, text="Clear Notepad", command=lambda: clear_notepad(textbox))
    clear_button.grid(row=1, column=0, padx=(20, 10), pady=(0, 20))

    # Bind the closing event of the window to the on_close function
    notepad.protocol("WM_DELETE_WINDOW", on_close)

    notepad.mainloop()
    notepad.quit()