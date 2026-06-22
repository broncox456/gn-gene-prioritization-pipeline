Write-Host "================================="
Write-Host " GN GENE PRIORITIZATION PIPELINE "
Write-Host "================================="

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

if (!(Test-Path "logs")) {
    New-Item -ItemType Directory -Path "logs" | Out-Null
}

$logfile = ".\logs\runlog_$timestamp.txt"

py .\scripts\05_download_real_geo.py > $logfile 2>&1
py .\scripts\01_prioritize_genes.py >> $logfile 2>&1
py .\scripts\02_validate_output.py >> $logfile 2>&1
py .\scripts\03_plot_top_genes.py >> $logfile 2>&1

$Rscript = Get-Command Rscript -ErrorAction SilentlyContinue

if ($Rscript) {
    Rscript .\scripts\r_analysis\exploratory_analysis.R >> $logfile 2>&1
} else {
    "Rscript not found. Exploratory R analysis was not executed." >> $logfile
}

Write-Host ""
Write-Host "Pipeline execution completed."
Write-Host "Logs saved in logs folder."
