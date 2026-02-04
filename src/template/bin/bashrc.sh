#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/env.sh"

msg="$(welcome_message)"

alacritty --hold --command bash -lc '
  i3-msg floating enable >/dev/null 2>&1 || true
  i3-msg fullscreen enable >/dev/null 2>&1 || true
  printf "%b\n" "$1"
' bash "$msg" &

