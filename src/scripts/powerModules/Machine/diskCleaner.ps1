# Function to clean up a specific item
function CleanUpItem($item, $path) {
    Write-Host "Cleaning up $item..."
    try {
        $fullPath = Join-Path $env:windir $path
        Remove-Item -Path "$fullPath\*" -Force -Recurse -ErrorAction Stop
        Start-Sleep -Seconds 1
        Write-Host "$item cleaned up successfully."
    }
    catch {
        Write-Host "Error cleaning up $item : $_"
    }
}

# Main function to perform disk cleanup
function DiskCleanerMachine {
    $cleanupItems = @(
        ("Windows Update Files", "SoftwareDistribution\Download"),
        ("Windows Error Reporting Files", "System32\winevt\Logs"),
        ("Windows Log Files", "System32\winevt\Logs")
        # Add more items and paths as needed
    )

    Write-Host "Disk Cleaner"
    Write-Host "============"
    Write-Host "This script will clean up the disk space on this machine."
    Write-Host "It will remove the following:"

    foreach ($item in $cleanupItems) {
        Write-Host "- $($item[0])"
    }

    Write-Host "`nThis script will take a while to complete."
    Write-Host "Please be patient.`n"

    # Request admin rights
    if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        $arguments = "& '${env:USERPROFILE}\Desktop\disk_cleaner.ps1'"
        Start-Process powershell -Verb runAs -ArgumentList $arguments
        Exit
    }

    Read-Host "Press Enter to continue."

    $progress = 1
    foreach ($item in $cleanupItems) {
        CleanUpItem $item[0] $item[1]
        $progress++
        if ($progress -le $cleanupItems.Count) {
            Read-Host "`nPress Enter to continue..."
        }
    }
}

# Run the main function
DiskCleanerMachine
