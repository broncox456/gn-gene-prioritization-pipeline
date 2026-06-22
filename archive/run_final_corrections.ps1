$ErrorActionPreference = "Stop"

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logFile = "logs\final_correction_run_$timestamp.log"

"Starting final correction run: $(Get-Date)" | Tee-Object -FilePath $logFile
"Project root: $(Get-Location)" | Tee-Object -FilePath $logFile -Append

py .\scripts\01_prioritize_genes.py 2>&1 | Tee-Object -FilePath $logFile -Append
py .\scripts\02_validate_output.py 2>&1 | Tee-Object -FilePath $logFile -Append
py .\scripts\03_plot_top_genes.py 2>&1 | Tee-Object -FilePath $logFile -Append
py .\scripts\07_generate_quantitative_outputs.py 2>&1 | Tee-Object -FilePath $logFile -Append
py .\scripts\08_generate_required_figures.py 2>&1 | Tee-Object -FilePath $logFile -Append
py .\scripts\09_generate_clinical_interpretation.py 2>&1 | Tee-Object -FilePath $logFile -Append

"Final correction run completed: $(Get-Date)" | Tee-Object -FilePath $logFile -Append

Get-ChildItem results -Recurse | Tee-Object -FilePath $logFile -Append
