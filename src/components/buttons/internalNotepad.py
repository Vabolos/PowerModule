import customtkinter
import tkinter.messagebox
import os

def save_text_locally(textbox):
    text_to_save = textbox.get("1.0", "end-1c")  # Get text from the textbox
    with open("saved_text.txt", "w") as file:
        file.write(text_to_save)
    tkinter.messagebox.showinfo("Save Successful", "Text saved locally as 'saved_text.txt'.")
    return

def load_saved_text(textbox):
    try:
        with open("saved_text.txt", "r") as file:
            saved_text = file.read()
            textbox.insert("1.0", saved_text)  # Insert the saved text into the textbox
    except FileNotFoundError:
        print("No saved text file found.")

def delete_saved_text(notepad):
    try:
        os.remove("saved_text.txt")
        tkinter.messagebox.showinfo("Delete Successful", "Saved text file deleted.")
        notepad.destroy()  # Close only the Notepad window after deleting the file
    except FileNotFoundError:
        tkinter.messagebox.showerror("Delete Failed", "No saved text file found.")

def close_notepad(notepad, textbox):
    # Function to be executed when attempting to close the window
    result = tkinter.messagebox.askyesnocancel("Close Notepad", "Do you want to save and quit?")

    if result:  # Save and quit
        save_text_locally(textbox)
        notepad.quit()
    elif result is False:  # Keep editing (False means 'No' was clicked)
        return

def open_notepad(self):
    notepad = customtkinter.CTk()
    notepad.title("Notepad")
    notepad.geometry(f"{800}x{600}")
    notepad.resizable(True, True)
    notepad.iconbitmap("powermodule.ico")

    textbox = customtkinter.CTkTextbox(notepad, width=750, height=500)
    textbox.grid(row=0, column=0, padx=20, pady=20)
    textbox.grid_rowconfigure(0, weight=1)
    textbox.grid_columnconfigure(0, weight=1)

    load_saved_text(textbox)

    notepad.protocol("WM_DELETE_WINDOW", lambda: close_notepad(notepad, textbox))

    # Delete button
    delete_button = customtkinter.CTkButton(notepad, text="Delete", command=lambda: delete_saved_text(notepad))
    delete_button.grid(row=1, column=0, padx=(20, 10), pady=(0, 20))

    notepad.mainloop()
    notepad.quit()
