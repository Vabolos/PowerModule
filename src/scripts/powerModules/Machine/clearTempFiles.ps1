param (
    [string]$WinVerPreference = "VISTA", # Default to newer OS
    [switch]$DryRun            # Enable dry run mode
)

# Log File
$LogFile = "C:\Temp\CleanupLog.txt"
if (-Not (Test-Path -Path $LogFile)) {
    New-Item -ItemType File -Path $LogFile | Out-Null
}

function Log-Message {
    param([string]$Message)
    Add-Content -Path $LogFile -Value "$(Get-Date): $Message"
}

function Remove-SubfoldersAndFiles {
    param (
        [string]$FolderRootPath
    )
    if (Test-Path -Path $FolderRootPath) {
        Log-Message "Attempting to purge $FolderRootPath"
        
        if ($DryRun) {
            Log-Message "Dry Run: Skipping actual deletion of $FolderRootPath"
            return
        }
        
        for ($i = 0; $i -lt 3; $i++) {
            try {
                Remove-Item -Recurse -Force -ErrorAction Stop -Path "$FolderRootPath\*"
                Log-Message "Successfully purged $FolderRootPath"
                return
            } catch {
                Log-Message "Attempt $($i + 1) failed for $FolderRootPath: $_"
                Start-Sleep -Seconds 5
            }
        }
        Log-Message "Failed to purge $FolderRootPath after 3 attempts"
    } else {
        Log-Message "Path not found: $FolderRootPath"
    }
}

function Invoke-ProfileFolder {
    param (
        [string]$FolderName
    )

    if (-Not (Test-Path -Path "$FolderName\ntuser.dat")) { return }
    $excludeList = @("Default", "Default User", "DefaultUser", "NetworkService", "LocalService")
    if ($excludeList -contains ([System.IO.Path]::GetFileName($FolderName))) { return }

    Log-Message "Processing profile folder: $FolderName"

    $UserProfilePath = $FolderName

    Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Temp"
    Remove-SubfoldersAndFiles "$UserProfilePath\AppData\LocalLow\Temp"
    # Add other folders here as needed...
}

# Determine OS Version
if ($WinVerPreference -eq "Unknown") {
    Log-Message "Unknown OS version, defaulting to VISTA"
    $WinVerPreference = "VISTA"
}

# User Profile Path
$UserProfileRootPath = if ($WinVerPreference -eq "XP") {
    "$env:SystemDrive\Documents and Settings"
} else {
    "$env:SystemDrive\Users"
}

# Clean System-Wide Temp Files
$SystemTempPaths = @(
    "$env:SystemDrive\Temp",
    "$env:SystemDrive\Windows\Temp",
    "$env:SystemDrive\Windows\Logs",
    "$env:SystemDrive\Windows\Prefetch"
    # Add additional paths as needed
)

foreach ($Path in $SystemTempPaths) {
    Remove-SubfoldersAndFiles $Path
}

# Process Each User Profile
Get-ChildItem -Path $UserProfileRootPath -Directory | ForEach-Object {
    Invoke-ProfileFolder -FolderName $_.FullName
}

Log-Message "Cleanup completed. Script execution finished."
Write-Output "Finished! Check log at $LogFile"
if (-Not $DryRun) { [Console]::ReadKey($true) }
