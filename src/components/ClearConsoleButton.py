def clear_console(self):
    self.textbox.configure(state="normal")
    self.textbox.delete("0.0", "end")
    self.textbox.configure(state="disabled")