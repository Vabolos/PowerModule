function Remove-SubfoldersAndFiles {
    param (
        [string]$FolderRootPath
    )
    # Confirm target folder exists
    if (Test-Path -Path $FolderRootPath) {
        # Make the folder to clean current and confirm it exists...
        Set-Location -Path $FolderRootPath
        # Confirm we switched directories
        if ($PWD.Path -eq $FolderRootPath) {
            # ...so that this command cannot delete the folder, only everything in it
            Write-Output "Purging $PWD"
            Remove-Item -Recurse -Force -ErrorAction SilentlyContinue *
        }
    }
}

function Process-ProfileFolder {
    param (
        [string]$FolderName
    )

    # Leave if it's not a user profile folder
    if (-Not (Test-Path -Path "$FolderName\ntuser.dat")) { return }

    # Leave if it's a profile folder on the exclude list
    $excludeList = @("Default", "Default User", "DefaultUser", "NetworkService", "LocalService")
    if ($excludeList -contains ([System.IO.Path]::GetFileName($FolderName))) { return }

    $UserProfilePath = $FolderName

    # Clean up these folders
    if ($WinVer -eq "XP") {
        Remove-SubfoldersAndFiles "$UserProfilePath\Local Settings\Temp"
        Remove-SubfoldersAndFiles "$UserProfilePath\Local Settings\Temporary Internet Files"
        Remove-SubfoldersAndFiles "$UserProfilePath\Application Data\Sun\Java\Deployment\cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\Local Settings\Temp\History"
        Remove-SubfoldersAndFiles "$UserProfilePath\Local Settings\Temp\Temporary Internet Files"
        Remove-SubfoldersAndFiles "$UserProfilePath\Local Settings\Application Data\Google\Chrome\User Data\Default\Cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\Local Settings\Application Data\Mozilla\Firefox\Profiles"
        Remove-SubfoldersAndFiles "$UserProfilePath\Local Settings\Application Data\Microsoft\Media Player\Art Cache"
    } else {
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Temp"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\LocalLow\Temp"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Windows\Temporary Internet Files"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Windows\INetCache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Windows\INetCache\IE"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Terminal Server Client\Cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Media Player"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Messenger"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Outlook\Offline Address Books"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Windows Live Contacts"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Windows\Explorer"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Windows\Explorer\IconCacheToDelete"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Windows\Explorer\ThumbCacheToDelete"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Windows\Burn"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Windows\History"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Windows\WER\ReportArchive"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Internet Explorer\Recovery\Active"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Internet Explorer\Recovery\Last Active"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Microsoft\Terminal Server Client\Cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Packages\Microsoft.MicrosoftEdge.Stable_8wekyb3d8bbwe\AC"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\CrashRpt"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\CrashDumps"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Downloaded Installations"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Adobe\Acrobat\9.0\Updater"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Adobe\Acrobat\9.0\Cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Adobe\Acrobat\10.0\Updater"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Adobe\Acrobat\10.0\Cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Adobe\Acrobat\11.0\Updater"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Adobe\Acrobat\11.0\Cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Adobe\Acrobat\DC\Updater"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Adobe\Acrobat\DC\Cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Google\Chrome\User Data\Default\Cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Opera Software\Opera Stable\Cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Mozilla\Firefox\Profiles"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\TechSmith\SnagIt\CrashDumps"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\TechSmith\SnagIt\Thumbnails"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\TechSmith\SnagIt\DataStore"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Local\Sap\SAP GUI\Traces"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Macromedia\Flash Player"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Adobe\Flash Player\AssetCache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Microsoft\Windows\Cookies"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Microsoft\Windows\PrivacIE"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Microsoft\Windows\IECompatCache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Microsoft\Windows\IETldCache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Microsoft\Teams\blob_storage"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Microsoft\Teams\cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Microsoft\Teams\databases"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Microsoft\Teams\gpucache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Microsoft\Teams\IndexedDB"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Microsoft\Teams\Local Storage"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\Roaming\Microsoft\Teams\tmp"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\LocalLow\Microsoft\CryptnetUrlCache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\LocalLow\Sun\Java\Deployment\cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\LocalLow\Sun\Java\Deployment\SystemCache"
        Remove-SubfoldersAndFiles "$UserProfilePath\AppData\LocalLow\Sun\Java\Deployment\javaws\cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\Application Data\Sun\Java\Deployment\cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\Application Data\Sun\Java\Deployment\SystemCache"
        Remove-SubfoldersAndFiles "$UserProfilePath\Application Data\Sun\Java\Deployment\javaws\cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\Application Data\Opera\Opera\cache"
        Remove-SubfoldersAndFiles "$UserProfilePath\Application Data\Microsoft\CryptnetUrlCache"
        Remove-SubfoldersAndFiles "$UserProfilePath\Application Data\Macromedia\Flash Player"
        Remove-SubfoldersAndFiles "$UserProfilePath\Application Data\Adobe\Flash Player\AssetCache"
    }
}

# Identify version of Windows
$WinVer = "Unknown"

$ver = (Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows NT\CurrentVersion").CurrentVersion
switch ($ver) {
    "5.1" { $WinVer = "XP" }
    "5.2" { $WinVer = "XP" }
    "6.0" { $WinVer = "VISTA" }
    "6.1" { $WinVer = "VISTA" }
    "6.2" { $WinVer = "VISTA" }
    "6.3" { $WinVer = "VISTA" }
    "10.0" { $WinVer = "VISTA" }
}

if ($WinVer -eq "Unknown") {
    $Response = Read-Host "Select OS  [X]P, [V]ista/7/8/8.1/10"
    if ($Response -eq "X") { $WinVer = "XP" }
    elseif ($Response -eq "V") { $WinVer = "VISTA" }
    else { Write-Output "Invalid response. Exiting."; exit }
}

# Set user profile path
if ($WinVer -eq "XP") {
    $UserProfileRootPath = "$env:SystemDrive\Documents and Settings"
} else {
    $UserProfileRootPath = "$env:SystemDrive\Users"
}

# Clean system-wide temp files
Remove-SubfoldersAndFiles "$env:SystemDrive\Temp"
Remove-SubfoldersAndFiles "$env:SystemDrive\ProgramData\Microsoft\Windows\WER"
Remove-SubfoldersAndFiles "$env:SystemDrive\ProgramData\Microsoft\Windows Defender\Scans\History\Results"
Remove-SubfoldersAndFiles "$env:SystemDrive\Program Files\Google\Update\Download"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\Prefetch"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\pchealth\ERRORREP"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\SoftwareDistribution\Download"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\ServiceProfiles\NetworkService\AppData\Local\Microsoft\Media Player\Art Cache"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\System32\spool\Printers"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\Temp"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\Logs"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\Debug"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\MiniDump"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\Downloaded Installations"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\SoftwareDistribution\DeliveryOptimization"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\Security\Logs"
Remove-SubfoldersAndFiles "$env:SystemDrive\Windows\System32\Wbem\Logs"

# Walk through each user profile folder
Get-ChildItem -Path $UserProfileRootPath -Directory | ForEach-Object {
    Process-ProfileFolder -FolderName $_.FullName
}

# Remove specific files
Remove-Item -Path "$env:AppData\Microsoft\Templates\~$normal.dot" -ErrorAction SilentlyContinue

Write-Output "Finished! Press a key to exit..."
[Console]::ReadKey($true)
