# Local GitLab CI/CD Pipeline Runner
param(
    [switch]$SkipRdf,
    [switch]$SkipValidate,
    [switch]$SkipCv,
    [switch]$SkipPages
)

$ErrorActionPreference = "Stop"
$startLocation = Get-Location
Set-Location $PSScriptRoot
$projectRoot = Get-Location

Write-Host "Starting local pipeline execution..." -ForegroundColor Magenta
Write-Host "Project root: $projectRoot" -ForegroundColor Magenta
Write-Host ""

try {
    # RDF Export Stage
    if (-not $SkipRdf) {
        Write-Host "" -ForegroundColor Cyan
        Write-Host "===================================================" -ForegroundColor Cyan
        Write-Host "STAGE: RDF Export (Docker)" -ForegroundColor Cyan
        Write-Host "===================================================" -ForegroundColor Cyan
        Write-Host ""
        
        $docker = Get-Command docker -ErrorAction SilentlyContinue
        if (-not $docker) {
            throw "Docker is required but not found"
        }
        
        Write-Host "Pulling Docker image: mathiasvda/logseq-rdf-export"
        docker pull mathiasvda/logseq-rdf-export
        if ($LASTEXITCODE -ne 0) { throw "Failed to pull Docker image" }
        
        Write-Host "Running logseq-rdf-export..."
        docker run --rm -v "${projectRoot}:/workspace" -w /workspace mathiasvda/logseq-rdf-export logseq-rdf-export matdata-expertise-raw.ttl --directory /workspace
        if ($LASTEXITCODE -ne 0) { throw "RDF export failed" }
        
        if (Test-Path "matdata-expertise-raw.ttl") {
            Write-Host "RDF export completed" -ForegroundColor Green
        } else {            throw "Output file not created"
        }
    }
    
    # Validate Stage
    if (-not $SkipValidate) {
        Write-Host "" -ForegroundColor Cyan
        Write-Host "===================================================" -ForegroundColor Cyan
        Write-Host "STAGE: Validate" -ForegroundColor Cyan
        Write-Host "===================================================" -ForegroundColor Cyan
        Write-Host ""
        
        if (-not (Test-Path "matdata-expertise-raw.ttl")) {
            throw "matdata-expertise-raw.ttl not found"
        }
        
        $venvPath = ".venv"
        if (-not (Test-Path $venvPath)) {
            Write-Host "Creating virtual environment..."
            python -m venv .venv
        }
        
        & ".venv\Scripts\Activate.ps1"
        
        Write-Host "Installing requirements..."
        pip install -q -r .\kg-actions\requirements.txt
        if ($LASTEXITCODE -ne 0) { throw "Failed to install requirements" }
        
        Write-Host "Cleaning graph..."
        python .\kg-actions\clean-graph.py
        if ($LASTEXITCODE -ne 0) { throw "Graph cleaning failed" }
        
        Write-Host "Validating graph..."
        python .\kg-actions\validate-graph.py
        if ($LASTEXITCODE -ne 0) { throw "Graph validation failed" }
        
        Write-Host "Validation completed" -ForegroundColor Green
    }
    
    # CV Generation Stage
    if (-not $SkipCv) {
        Write-Host "" -ForegroundColor Cyan
        Write-Host "===================================================" -ForegroundColor Cyan
        Write-Host "STAGE: CV Generation (Docker)" -ForegroundColor Cyan
        Write-Host "===================================================" -ForegroundColor Cyan
        Write-Host ""
        
        if (-not (Test-Path "matdata-expertise.ttl")) {
            throw "matdata-expertise.ttl not found"
        }
        
        $docker = Get-Command docker -ErrorAction SilentlyContinue
        if (-not $docker) {
            throw "Docker is required but not found"
        }
        
        Write-Host "Pulling Docker image: mathiasvda/rendercv-with-profile-pic"
        docker pull mathiasvda/rendercv-with-profile-pic
        if ($LASTEXITCODE -ne 0) { throw "Failed to pull Docker image" }
        
        Write-Host "Running complete-cv.py..."
        docker run --rm -v "${projectRoot}:/workspace" -w /workspace/cv mathiasvda/rendercv-with-profile-pic /bin/sh -c "pip install -q -r requirements.txt; python3.12 ./complete-cv.py"
        if ($LASTEXITCODE -ne 0) { throw "CV completion failed" }
        
        Write-Host "Rendering CV..."
        docker run --rm -v "${projectRoot}:/workspace" -w /workspace/cv mathiasvda/rendercv-with-profile-pic rendercv render -nomd -nohtml -nopng Mathias_Vanden_Auweele_CV.yaml
        if ($LASTEXITCODE -ne 0) { throw "CV rendering failed" }
        
        Write-Host "CV generated successfully" -ForegroundColor Green
    }
    
    # Summary
    Write-Host "" -ForegroundColor Magenta
    Write-Host "===================================================" -ForegroundColor Magenta
    Write-Host "PIPELINE COMPLETED SUCCESSFULLY" -ForegroundColor Magenta
    Write-Host "===================================================" -ForegroundColor Magenta
    Write-Host ""
    Write-Host "You can now safely push your changes to GitLab" -ForegroundColor Green
    Write-Host ""
    
} catch {
    Write-Host "" -ForegroundColor Red
    Write-Host "===================================================" -ForegroundColor Red
    Write-Host "PIPELINE FAILED" -ForegroundColor Red
    Write-Host "===================================================" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    Write-Host $_.ScriptStackTrace -ForegroundColor Red
    exit 1
} finally {
    Set-Location $startLocation
}
