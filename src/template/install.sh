#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/bin/env.sh"

"${ROOT}/bin/welcome.sh"
"${ROOT}/bin/bashrc.sh"
"${ROOT}/bin/screen_saver.sh"

firefox --new-window "${ROOT}/static/subjects"

nix profile add .#default

nohup pycharm &>/dev/null &

pkill -ox alacritty
