import subprocess
import threading
import queue
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from pygments.lexers.shell import BashLexer
from tkinter import END

class PowerShellCompleter(Completer):
    def __init__(self):
        self.commands = ["cls", "dir", "cd", "echo"]

    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        for command in self.commands:
            if command.startswith(word_before_cursor):
                yield Completion(command, start_position=-len(word_before_cursor))

class AppFunctions:
    def __init__(self, app_instance):
        self.app_instance = app_instance
        self.is_powershell_open = False  # Flag to track if PowerShell console is open
        self.input_queue = queue.Queue()

    def execute_command(self, event):
        self.app_instance.textbox.configure(state="normal")
        self.app_instance.textbox.delete("0.0", "end")
        # Get the command from the entry widget
        command = self.app_instance.entry.get()

        if command.strip().lower() == 'cls':
            self.app_instance.textbox.delete("0.0", "end")
            self.app_instance.entry.delete(0, "end")
            return

        if command.strip().lower() == 'powershell':  # Open PowerShell console
            self.start_powershell_console()
            self.app_instance.entry.delete(0, "end")
            return

        if self.is_powershell_open and command.strip().lower() == 'exit':  # Close PowerShell console
            self.is_powershell_open = False
            self.app_instance.textbox.insert("end", "PowerShell console closed.\n")
            self.app_instance.entry.delete(0, "end")
            return

        # Start a new process and run it in a separate thread
        self.app_instance.process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

        # Start a separate thread to read and display the output in real-time
        threading.Thread(target=self.update_output).start()

        # Clear the entry widget for the next command
        self.app_instance.entry.delete(0, "end")

    def update_output(self):
        # Read the output line by line
        for line in self.app_instance.process.stdout:
            # Append the line to the textbox
            self.app_instance.textbox.configure(state="normal")
            self.app_instance.textbox.insert("end", line)
            self.app_instance.textbox.configure(state="disabled")

    def process_command(self, command):
        try:
            # Execute the command using subprocess
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            # If there's an error, capture the output
            result = e.output

        return result

    def start_powershell_console(self):
        if not self.is_powershell_open:
            self.is_powershell_open = True
            self.app_instance.textbox.insert("end", "PowerShell console opened. Type 'exit' to close.\n\n")

            completer = PowerShellCompleter()
            style = Style.from_dict({
                'prompt': '#00aa00',
                'command': '#0000aa',
                'output': '#aa0000',
            })

            def get_input():
                prompt_text = "\n\nPS> "
                self.app_instance.textbox.insert("end", prompt_text)
                return self.app_instance.textbox.get("end-1c linestart", "end-1c lineend")

            session = PromptSession(completer=completer, lexer=PygmentsLexer(BashLexer), style=style, input=get_input)

            def handle_powershell_command():
                text = self.app_instance.textbox.get("end-1c linestart", "end-1c lineend")
                text = text.strip()
                if text.lower() == "exit":
                    self.is_powershell_open = False
                    self.app_instance.textbox.insert("end", "\nPowerShell console closed.\n")
                elif text.lower() == "powershell":
                    self.app_instance.textbox.delete("end-1c wordstart", "end")
                else:
                    output = self.process_command(text)
                    self.app_instance.textbox.configure(state="normal")
                    self.app_instance.textbox.insert("end", output + "\n")
                    self.app_instance.textbox.configure(state="disabled")
                    self.app_instance.textbox.see("end")

            def on_enter(event):
                handle_powershell_command()
                self.app_instance.entry.delete(0, "end")

            self.app_instance.entry.bind("<Return>", on_enter)
            # Insert PS> prompt
            self.app_instance.textbox.insert("end", "PS> ")
        else:
            self.app_instance.textbox.insert("end", "PowerShell console is already open.\n")

