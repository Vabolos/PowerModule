Get-ADUser -Filter {Enabled -eq $false} | Select-Object Name, SamAccountName
