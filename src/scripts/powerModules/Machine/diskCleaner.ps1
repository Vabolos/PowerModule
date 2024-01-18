# disk_cleaner.ps1

# Function to clean up a specific item
function CleanUpItem($item, $path) {
    Write-Host "Cleaning up $item..."
    Remove-Item -Path "$env:windir\$path\*" -Force -Recurse -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 1
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
