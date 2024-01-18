# disk cleaner script
from tkinter import messagebox
import subprocess

def disk_cleaner_machine():
    powershell_script_path = r'src/scripts/powermodules/Machine/diskCleaner.ps1'
    
    # Count the number of cleanup items in the PowerShell script
    cleanup_items_count = subprocess.check_output(['powershell.exe', '-File', powershell_script_path, '-Count']).decode('utf-8').strip()

    print("Disk Cleaner")
    print("============")
    print("This script will clean up the disk space on this machine.")
    print(f"It will remove {cleanup_items_count or 0} items.")
