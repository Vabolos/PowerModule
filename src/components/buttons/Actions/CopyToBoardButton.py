def copy_to_clipboard(self):
    self.clipboard_clear()
    self.clipboard_append(self.textbox.get("0.0", "end"))
    print("Copied text to clipboard.")