#!/bin/sh

create_output_path
download_zip >/dev/null
#append_to_bashrc
install_pycharm >/dev/null
setup_pycharm
create_venv >/dev/null
open_firefox >/dev/null &
open_pycharm >/dev/null 2>&1 &
open_popup "$(welcome_message)" &
clean_source_folder

# Exit shell only in non debug mode
if [[ -z "${DEBUG:-}" ]]; then
    exit_current_shell
fi
