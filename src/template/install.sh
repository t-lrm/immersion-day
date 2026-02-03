#!/bin/sh

set -euo pipefail

CONTACT="timothee.le-roux-maertens@epita.fr"

# Host informations (substituted by docker/entrypoint.sh)
IP="__IP__"
PORT="__PORT_ZIP__"
SUBJECTS_URL="http://__IP__:__PORT_SUBJECTS__"

OUT_PATH="${HOME}/ji"
PYCHARM_CONSENT_DIR="${OUT_PATH}/client_files/pycharm-consent"
SUBJECTS_DIR="${OUT_PATH}/ci-imported"
MOULINETTE_DIR="${OUT_PATH}/client_files/Moulinette"
TOOLS_DIR="${OUT_PATH}/client_files/tools"

ZIP_NAME="bundle.zip"

MOD="win"

PYCHARM="pycharm"
PIP_PACKAGES=(pygame pyfiglet keyboard)

shortcuts_message() {
  cat <<EOF
Voici le kit de survie pour vous familiariser avec votre nouvel environnement :

  $MOD + D           : Chercher un programme
  $MOD + Shift + Q   : Fermer une fenêtre
  $MOD + [number]    : Accéder au workspace n°[number]
  $MOD + Entrée      : Ouvrir un nouveau terminal

Commandes shell utiles (à faire dans un terminal) :
  ls                 : Lister les fichiers du dossier actuel
  cd                 : Se déplacer dans les dossiers
  aled               : Afficher ces commandes
EOF
}

welcome_message() {
    cat <<EOF
Bonjour et bienvenue en séance de TP !

Aujourd'hui vous allez faire un TP en python. Comme remarqué nous ne sommes pas sous Windows, bienvenue sur NixOS !

$(shortcuts_message)

Tu peux désormais appuyer sur $MOD + Shift + Q pour fermer cette fenêtre, et n'hésitez pas à solliciter les assistants si tu as besoin d'aide ou que tu as des questions :)
EOF
}

bashrc_extension() {
    cat <<EOF
alias aled="echo -e '${shortcut_message}'"
alias aled="echo -e '${shortcut_message}'"
alias sujets="firefox ${SUBJECTS_URL}"
EOF
}

#!/bin/sh

# If you want to use this function with curl, you need to run something like this:
# curl -s ip:port | DEBUG=1 sh
debug() {
  [[ -n "${DEBUG:-}" ]] || return 0
  printf '[%(%F %T)T] %s\n' -1 "$*" >&2
}

create_output_path() {
    local RESET="\033[0m"
    local YELLOW="\033[33m"
    local CYAN="\033[36m"

    if [ -d "$OUT_PATH" ]; then
        echo -e "${YELLOW}WARNING:${RESET} The folder ${OUT_PATH} already exists."
        printf "${CYAN}Do you want to continue? (y/n)${RESET} "
        IFS= read -n 1 -r REPLY < /dev/tty
        echo "" # add a breakline
        case "$REPLY" in
            [Yy]);;
            *) echo "Aborting."; exit 1 ;;
        esac
    fi

    rm -rf "$OUT_PATH"
    mkdir -p "$OUT_PATH"
}


download_zip() {
    debug "Downloading zip..."
    curl -s "http://$IP:$PORT" --output "$OUT_PATH/$ZIP_NAME"
    unzip "$OUT_PATH/$ZIP_NAME" -d "$OUT_PATH"
    rm "$OUT_PATH/$ZIP_NAME"
}

append_to_bashrc() {
    debug "Adding new aliases to ~/.bashrc..."
    printf '%s\n' "$(bashrc_extension)" >> "$HOME/.bashrc"
}

install_pycharm() {
    debug "Installing Pycharm..."
    NIXPKGS_ALLOW_UNFREE=1 nix profile add --impure nixpkgs#jetbrains."${PYCHARM}"
}

setup_pycharm() {
    debug "Setting up Pycharm..."
    mkdir -p "$HOME/.local/share/JetBrains/consentOptions"
    mkdir -p "$HOME/.config/JetBrains/PyCharmCE2024.3/options"
    mkdir -p "$HOME/.java"

    cp "${PYCHARM_CONSENT_DIR}/accepted" "$HOME/.local/share/JetBrains/consentOptions/"
    cp "${PYCHARM_CONSENT_DIR}/trusted-paths.xml" "$HOME/.config/JetBrains/PyCharmCE2024.3/options/"
    cp "${PYCHARM_CONSENT_DIR}/jdk.table.xml" "$HOME/.config/JetBrains/PyCharmCE2024.3/options/"
    cp -r  "${PYCHARM_CONSENT_DIR}/.userPrefs" "$HOME/.java/"

    cp -r "${MOULINETTE_DIR}" "${SUBJECTS_DIR}"
    cp -r "${TOOLS_DIR}" "${SUBJECTS_DIR}"
}

create_venv() {
    debug "Creating venv..."
    python3 -m venv "$OUT_PATH/.venv"
    source "$OUT_PATH/.venv/bin/activate"
    pip install --upgrade pip
    pip install "${PIP_PACKAGES[@]}"
    deactivate
}

open_firefox() {
    debug "Opening Firefox..."
    firefox --new-window "${SUBJECTS_URL}"
}

open_pycharm() {
    debug "Opening Pycharm..."
    "$PYCHARM" "$SUBJECTS_DIR"
}

open_popup() {
    debug "Opening welcome message..."
    local message="$1"
    alacritty --hold --command sh -c 'i3-msg floating enable >/dev/null 2>&1; printf "%b\n" "$1"' sh "$message"
}

clean_source_folder() {
    debug "Cleaning source folder..."
    rm -rf -- "${PYCHARM_CONSENT_DIR}"
}

exit_current_shell() {
    debug "Killing oldest alacritty session..."
    pkill -ox alacritty
}

