#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

show_welcome() {
  i3-msg floating enable >/dev/null 2>&1 || true
  printf '%b\n' "$welcome_message"
}

alacritty --hold --command bash -lc "$(declare -f show_welcome); show_welcome" &

