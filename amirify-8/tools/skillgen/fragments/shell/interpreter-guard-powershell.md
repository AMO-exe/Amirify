```powershell
if (-not (Test-Path amirify-out\.amirify_python)) {
    $AMIRIFY_PYTHON = $null
    $amirifyCmd = Get-Command amirify -ErrorAction SilentlyContinue
    if ($amirifyCmd) {
        # The interpreter that owns the amirify entry point sits next to it
        # (<env>\Scripts\python.exe for uv tool, pipx, and venv installs).
        $py = Join-Path (Split-Path $amirifyCmd.Source) "python.exe"
        if (Test-Path $py) { $AMIRIFY_PYTHON = $py }
    }
    if (-not $AMIRIFY_PYTHON) { $AMIRIFY_PYTHON = "python" }
    New-Item -ItemType Directory -Force -Path amirify-out | Out-Null
    & $AMIRIFY_PYTHON -c "import sys; open('amirify-out/.amirify_python', 'w', encoding='utf-8').write(sys.executable)"
}
```
