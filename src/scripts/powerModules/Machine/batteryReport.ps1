# Define the output directory
$outputDir = "C:\Temp"

# Check if the directory exists
if (-not (Test-Path -Path $outputDir -PathType Container)) {
    # If not, create the directory
    New-Item -Path $outputDir -ItemType Directory | Out-Null
}

# Define the output path for the battery report
$outputPath = Join-Path -Path $outputDir -ChildPath "Battery-Report.html"

# Generate the battery report
Write-Host "Generating battery report..."
Invoke-Expression -Command "powercfg /batteryreport /output `"$outputPath`""
Write-Host "Opening battery report..."
# start counting for 5 seconds
$counter = 5
while ($counter -gt 0) {
    Write-Host "Opening report in $counter seconds..."
    Start-Sleep -Seconds 1
    $counter--
}
# open the battery report in the default web browser
Invoke-Expression -Command "Start-Process `"$outputPath`""
