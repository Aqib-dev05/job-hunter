#!/usr/bin/env bash
# Starts Job Hunter on Linux. The first run also sets everything up:
#   - a virtual environment in .venv (it can see the system's GTK/Qt packages)
#   - pywebview from requirements.txt
#   - the window's page (ui/dist), built with npm
# Later runs just open the window.
set -euo pipefail
cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"

PYTHON="${PYTHON:-python3}"
if ! command -v "$PYTHON" >/dev/null 2>&1; then
    echo "Python 3.10+ was not found. Install it first (for example: sudo apt install python3 python3-venv)." >&2
    exit 1
fi
if ! "$PYTHON" -c 'import sys; sys.exit(sys.version_info < (3, 10))'; then
    echo "Job Hunter needs Python 3.10 or newer; $("$PYTHON" --version 2>&1) was found." >&2
    exit 1
fi

if [ ! -x .venv/bin/python ]; then
    echo "Setting up the Python environment (first run only)..."
    # --system-site-packages: PyGObject (GTK) comes from the distribution, not from pip.
    "$PYTHON" -m venv --system-site-packages .venv || {
        echo "Could not create the virtual environment. On Debian/Ubuntu: sudo apt install python3-venv" >&2
        exit 1
    }
fi

# Reinstall only when requirements.txt changed.
if ! cmp -s requirements.txt .venv/.requirements.installed; then
    .venv/bin/python -m pip install --quiet -r requirements.txt
    cp requirements.txt .venv/.requirements.installed
fi

if [ ! -f ui/dist/index.html ]; then
    if ! command -v npm >/dev/null 2>&1; then
        echo "Node.js 20+ is needed once to build the window (https://nodejs.org). Install it and run ./run.sh again." >&2
        exit 1
    fi
    echo "Building the window (first run only)..."
    (cd ui && npm ci --no-audit --no-fund && npm run build)
fi

exec .venv/bin/python -I webapp.py "$@"
