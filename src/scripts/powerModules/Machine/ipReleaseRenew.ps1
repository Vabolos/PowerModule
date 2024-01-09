# script to release and renew IP address


# Release IP address
ipconfig /release

# Wait for 5 seconds
Start-Sleep -s 3

# Renew IP address
ipconfig /renew