#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/env.sh"

{
  echo "aled() {"
  echo "  cat <<'EOF'"
  shortcuts_message
  echo "EOF"
  echo "}"
} >> "$HOME/.bashrc"
