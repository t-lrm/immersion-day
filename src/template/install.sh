#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/bin/env.sh"

"${ROOT}/bin/welcome.sh"
"${ROOT}/bin/bashrc.sh"
"${ROOT}/bin/screen_saver.sh"
"${ROOT}/bin/host.sh"

nohup firefox --new-window "${ROOT}/static/subjects"

# 'add' doesn't work on PIE computers
nix profile install .#default

nohup pycharm &>/dev/null &

pkill -ox alacritty
