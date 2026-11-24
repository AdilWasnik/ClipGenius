# ClipGenius launcher (Windows). Creates .venv on first run, starts the app, opens the browser.
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (-not (Test-Path .venv/Scripts/python.exe)) {
    python -m venv .venv
    .venv/Scripts/python.exe -m pip install -r requirements.txt
}
$port = if ($env:CLIPGENIUS_PORT) { $env:CLIPGENIUS_PORT } elseif ($env:NEONCLIPPING_PORT) { $env:NEONCLIPPING_PORT } else { $null }
if (-not $port) {
    $port = 8770
    $busy = Get-NetTCPConnection -LocalPort 8770 -State Listen -ErrorAction SilentlyContinue
    if ($busy) { $port = 8771 }
    $env:CLIPGENIUS_PORT = "$port"
}
Start-Process "http://127.0.0.1:$port"
.venv/Scripts/python.exe app.py
