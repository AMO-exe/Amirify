```bash
if [ ! -f amirify-out/.amirify_python ]; then
    AMIRIFY_BIN=$(which amirify 2>/dev/null)
    if [ -n "$AMIRIFY_BIN" ]; then
        PYTHON=$(head -1 "$AMIRIFY_BIN" | tr -d '#!')
        case "$PYTHON" in *[!a-zA-Z0-9/_.@-]*) PYTHON="python3" ;; esac
    else
        PYTHON="python3"
    fi
    mkdir -p amirify-out
    "$PYTHON" -c "import sys; open('amirify-out/.amirify_python', 'w', encoding='utf-8').write(sys.executable)"
fi
```
