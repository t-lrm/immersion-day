#!/usr/bin/env bash
set -euo pipefail

REPORTS="${HOME}/ji/reports"

mkdir -p "$REPORTS"
python3 -m http.server 42999 --directory "$REPORTS" >/dev/null 2>&1 &
