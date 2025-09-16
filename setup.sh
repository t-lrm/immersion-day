#!/bin/sh

# ===== VARIABLES =====

CONTACT="timothee.le-roux-maertens@epita.fr"

URL_MARIO="https://github.com/t-lrm/mario-python.git"
URL_CHIP8="https://github.com/t-lrm/chip-8.git"
TOKEN="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"

OUT_PATH="$HOME/subjects"

ALACRITTY_PID=$(pgrep -o -x alacritty)

MOD="win"

CMD_LIST="Voici le kit de survie pour vous familiariser avec votre nouvel environnement :\n
\t$MOD + d: chercher un programme.\n
\t$MOD + shift + q: fermer une fenêtre.\n
\t$MOD + [number]: accéder au workspace n°[number].\n
\t$MOD + entrée: ouvrir un nouveau terminal.\n
\tls: lister les fichiers du dossier actuel.\n
\tcd: rentrer dans les fichiers.\n
\tide: lancer l'IDE pycharm (a faire dans un terminal)\n
\taled: afficher ces commandes."

INIT_TEXT="Bonjour et bienvenue en séance de TP !\n\n"\
"Aujourd'hui vous allez faire un TP en python. Comme remarqué nous ne sommes pas sous Windows, bienvenue sur NixOS !\n\n"\
"$CMD_LIST\n\n"\
"----------------------------------------------\n\n"\
"\t$MOD + shift + q pour fermer cette fenêtre, et n'hésitez pas à nous solliciter :)"

INIT_CMD="i3-msg floating enable > /dev/null && echo -e \"$INIT_TEXT\" && kill \"$ALACRITTY_PID\""

PYTHON3_PATH=$(whereis python3 | cut -d' ' -f2 | head -n1)
ALIAS_ALED="alias aled=\"echo -e \\\"$CMD_LIST\\\"\""
ALIAS_IDE="alias ide=\"(export PYCHARM_PYTHON_PATH=$PYTHON3_PATH && nohup pycharm-community ~/subject < /dev/null > /dev/null 2>&1 &) && exit\""

# ===== WARNING =====

# Show a warning if the output path already exists
if [ -d "$OUT_PATH" ]; then
    echo -e "\e[33mWarning:\e[0m This script will erase the content of '$OUT_PATH' if it exists."
    read -p "Do you want to continue? (y/n) " -n 1 -r
    echo   # move to a new line

    if [[ ! $REPLY =~ ^[Yy]$ ]]
    then
        echo "Aborting."
        exit 1
    fi
fi

# ===== SETUP =====

# Clean and create output path
rm -rf "$OUT_PATH"
mkdir -p "$OUT_PATH"

# Add aliases to bashrc
echo $ALIAS_ALED >> ~/.bashrc
echo $ALIAS_IDE >> ~/.bashrc

# Install pycharm
if [ -f /etc/NIXOS ]; then
    echo "INFO: Installing Pycharm..."
    export NIXPKGS_ALLOW_UNFREE=1
    nix profile install nixpkgs#jetbrains.pycharm-community --impure
fi

# ===== DOWNLOAD SUBJECTS =====

if [ -z "$TOKEN" ]; then
    echo -e "\e[31mError:\e[0m No token provided. Please contact $CONTACT to get one."
    exit 1
fi

# WARNING: putting tokens in URLs can leak via bash history/logs
echo "INFO: Cloning Mario Python..."
git clone "https://epita:${TOKEN}@github.com/t-lrm/mario-python.git" "$OUT_PATH" 2> git_error.log

echo "INFO: Cloning Chip 8..."
git clone "https://epita:${TOKEN}@github.com/t-lrm/chip-8.git" "$OUT_PATH/sujet-3" 2>> git_error.log
history -c

if grep -q "Authentication failed" git_error.log || grep -q "access denied" git_error.log; then
    echo -e "\e[31mError:\e[0m The provided token is expired or invalid. Please contact $CONTACT to get a new one."
    exit 1
fi

cat git_error.log
rm -f git_error.log

# ===== OPEN TERMINAL =====

# Open terminal
nohup alacritty --hold -e sh -c "$INIT_CMD" &> /dev/null

# Clean history
history -c
