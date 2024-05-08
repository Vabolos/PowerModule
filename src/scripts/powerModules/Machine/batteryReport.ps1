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
Invoke-Expression -Command "powercfg /batteryreport /output `"$outputPath`""
