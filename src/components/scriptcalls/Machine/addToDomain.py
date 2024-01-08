import customtkinter
import subprocess

# function + window to add a machine to the domain
def add_to_domain_machine(self):
    self.textbox.configure(state="normal")

    # Get the input from the dialog
    dialog = customtkinter.CTkInputDialog(text="Machine name:", title="addToDomain")
    machine_name = dialog.get_input()

    # Specify the path to your PowerShell script
    powershell_script = r'src/scripts/powermodules/Machine/addToDomain.ps1'

    try:
        # Run the PowerShell script and pass the input as a parameter
        scriptOutput = subprocess.check_output(['powershell', '-File', powershell_script, '-machineName', machine_name], text=True, stderr=subprocess.STDOUT)

        # Update the text in the custom Textbox with the PowerShell script output
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", scriptOutput)
    except subprocess.CalledProcessError as e:
        # Handle any errors that occurred during script execution
        self.textbox.insert("0.0", f"Error: {e.output}")
    finally:
        # Update the state of the custom Textbox to disabled
        self.textbox.configure(state="disabled")