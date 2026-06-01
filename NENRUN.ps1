Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force
& "c:\Users\VyshnaviSuram\automation\NEN Automation-framework\.venv\Scripts\Activate.ps1"
Write-Host "Activated VENV"

$ErrorActionPreference = "Continue"
$jsonReportDir = "reports/json-report"
New-Item -ItemType Directory -Path $jsonReportDir -Force | Out-Null
Get-ChildItem -Path $jsonReportDir -Filter "*.json" -ErrorAction SilentlyContinue | Remove-Item -Force

$htmlReportDir = "reports/html-report/personas"
New-Item -ItemType Directory -Path $htmlReportDir -Force | Out-Null
Get-ChildItem -Path $htmlReportDir -Filter "*.html" -ErrorAction SilentlyContinue | Remove-Item -Force

$runs = @(
    @{ USER_TYPE = "prod_student";              feature = "features/student.feature"        ; name = "student" },
    @{ USER_TYPE = "prod_faculty";              feature = "features/faculty.feature"        ; name = "faculty" },
    @{ USER_TYPE = "prod_mentor";               feature = "features/mentor.feature"         ; name = "mentor" },
    @{ USER_TYPE = "prod_rm";                   feature = "features/rm.feature"             ; name = "rm" },
    @{ USER_TYPE = "prod_incubator";            feature = "features/incubator.feature"      ; name = "incubator" },
    @{ USER_TYPE = "prod_viability_specialist"; feature = "features/viability.feature"      ; name = "viability" },
    @{ USER_TYPE = "prod_cohort_manager";       feature = "features/cohort_manager.feature" ; name = "cohort_manager" },
    @{ USER_TYPE = "prod_evaluator";            feature = "features/evaluator.feature"      ; name = "evaluator" }
)

$failed = @()

foreach ($run in $runs) {
    Get-Process -Name "chrome","chromium" -ErrorAction SilentlyContinue |
        Where-Object { $_.MainWindowTitle -eq "" } |
        Stop-Process -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 4

    $env:USER_TYPE = $run.USER_TYPE
    Write-Host "`nRunning: $($run.feature) as $($run.USER_TYPE)"
    $jsonOut = Join-Path $jsonReportDir "$($run.name).json"
    $htmlOut = Join-Path $htmlReportDir "$($run.name).html"
    .\.venv\Scripts\python.exe -m behave $run.feature `
        -f allure_behave.formatter:AllureFormatter -o reports/allure-results `
        -f json.pretty                            -o $jsonOut `
        -f behave_html_formatter:HTMLFormatter    -o $htmlOut `
        --no-capture
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "FAILED: $($run.feature)"
        $failed += $run.feature
    }
}

Write-Host "`nGenerating one combined HTML report from all persona HTML outputs..."
.\.venv\Scripts\python.exe scripts/combine_persona_reports.py "reports/html-report/personas" "reports/html-report/combined_report.html"
$reportExitCode = $LASTEXITCODE

deactivate

if ($reportExitCode -ne 0) {
    Write-Host "`nFeature runs completed, but combined HTML report generation failed."
    exit $reportExitCode
} elseif ($failed.Count -gt 0) {
    Write-Host "`nThe following features had failures:"
    $failed | ForEach-Object { Write-Host "  - $_" }
    Write-Host "`nCombined report saved to: reports/html-report/combined_report.html"
    exit 1
} else {
    Write-Host "`nAll features passed."
    Write-Host "Combined report saved to: reports/html-report/combined_report.html"
    exit 0
}
