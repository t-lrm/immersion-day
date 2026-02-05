#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/bin/env.sh"

"${ROOT}/bin/welcome.sh"
"${ROOT}/bin/bashrc.sh"

firefox --new-window "${ROOT}/static/subjects"

nix profile add .#default

pycharm & 2>&1 /dev/null

pkill -ox alacritty
