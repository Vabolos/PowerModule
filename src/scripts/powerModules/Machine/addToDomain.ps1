# add machine to domain
# Parameters:
#   $domainName - domain name
#   $domainUser - domain user
#   $domainPassword - domain password

param(
    [Parameter(Mandatory=$true)]
    [string]$domainName,
    [Parameter(Mandatory=$true)]
    [string]$domainUser,
    [Parameter(Mandatory=$true)]
    [pscredential]$domainPassword
)

$domain = $domainName
$user = $domainUser
$password = $domainPassword

$secpasswd = ConvertTo-SecureString $password -AsPlainText -Force

$mycreds = New-Object System.Management.Automation.PSCredential ($user, $secpasswd)

Add-Computer -DomainName $domain -Credential $mycreds -Restart -Force
