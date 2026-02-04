#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/bin/env.sh"

"${ROOT}/bin/welcome.sh"
"${ROOT}/bin/bashrc.sh"

firefox --new-window "${ROOT}/static/subjects"

pkill -ox alacritty

