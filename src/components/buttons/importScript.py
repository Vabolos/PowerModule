import filecmp
import fileinput
import subprocess
import tkinter as tk
from tkinter import messagebox

def import_script(self):
    subprocess.Popen(r'explorer /select')
    # only accept .ps1 files (only show these files in the file explorer)
    if filecmp.endswith(".ps1"):
        # open the file
        with open(fileinput, "r") as f:
            # read the file
            data = f.read()
            # insert the data into the console
            self.consoleEntry.insert(tk.END, data)
            # insert a new line
            self.consoleEntry.insert(tk.END, "\n")
            # focus the console
            self.consoleEntry.focus()
            # set the cursor to the end of the console
            self.consoleEntry.see(tk.END)
            # update the console
            self.consoleEntry.update()
    else:
        # if the file is not a .ps1 file, show an error
        messagebox.showerror("Error", "Only .ps1 files are supported!")
        # focus the console
        self.consoleEntry.focus()
        # set the cursor to the end of the console
        self.consoleEntry.see(tk.END)
        # update the console
        self.consoleEntry.update()