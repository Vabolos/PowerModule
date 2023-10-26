import subprocess

# List of modules
modules = [
    "testModule",
    "testModule2",
    "testModule3",
    "testModule4",
]

# Path to PowerShell scripts folder
script_folder = "src\\script\\powerModules\\"

for module in modules:
    # Build the path to the PowerShell script
    script_path = script_folder + module + ".ps1"
