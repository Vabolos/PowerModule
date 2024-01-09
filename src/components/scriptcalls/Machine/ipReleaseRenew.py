import customtkinter
import subprocess

# function + window to release/renew the IP address of a machine
def ip_release_renew(self):
    self.textbox.configure(state="normal")

    # Get the input from the dialog

    # specify script path to get the hostname and pass it to the dialog
    powershell_script = r'src/scripts/getHostname.ps1'
    Hostname = subprocess.check_output(['powershell', '-File', powershell_script], text=True, stderr=subprocess.STDOUT)

    dialog = customtkinter.CTkInputDialog(text=f"Hostname:\n\nHostname = {Hostname}", title="ipReleaseRenew")
    machine_name = dialog.get_input()

    # Specify the path to your PowerShell script
    powershell_script = r'src/scripts/powermodules/Machine/ipReleaseRenew.ps1'

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