#!/usr/bin/env bash
set -euo pipefail

ROOT="${HOME}/ji"
ZIP="bundle.zip"
IP="192.168.1.17"
PORT="42001"

mkdir "$ROOT"
cd "$ROOT"
curl -L "http://${IP}:${PORT}" -o "$ZIP"
unzip "$ZIP"

./install.sh
