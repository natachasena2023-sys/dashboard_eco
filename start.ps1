Write-Host "============================================"
Write-Host "   Iniciando Dashboard Eco (Streamlit)"
Write-Host "============================================"
Write-Host ""

$projectPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $projectPath

# Activar entorno virtual
$venvPath = ".\.venv\Scripts\Activate.ps1"

if (Test-Path $venvPath) {
    Write-Host "Activando entorno virtual..."
    . $venvPath
} else {
    Write-Host "ERROR: No se encontró el entorno virtual (.venv)"
    Write-Host "Crea uno con: python -m venv .venv"
    exit
}

Write-Host "Limpiando cache de Streamlit..."
streamlit cache clear

Write-Host "Lanzando aplicación Streamlit..."
streamlit run main.py

Write-Host ""
Write-Host "Aplicación finalizada."
