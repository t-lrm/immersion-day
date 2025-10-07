#!/bin/sh

# ===== VARIABLES =====

CONTACT="timothee.le-roux-maertens@epita.fr"

# Host informations (substitute by server.py)
IP="__IP__"
PORT="__PORT__"

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
ALIAS_IDE="alias ide=\"(export PYCHARM_PYTHON_PATH=$PYTHON3_PATH && nohup pycharm-community $OUT_PATH < /dev/null > /dev/null 2>&1 &) && exit\""

# ===== WARNING =====

# Show a warning if the output path already exists
if [ -d "$OUT_PATH" ]; then
    echo -e "\e[33mWarning:\e[0m This script will erase the content of '$OUT_PATH' if it exists."
    read -p "Do you want to continue? (y/n) " -n 1 -r

    if [[ ! $REPLY =~ ^[Yy]$ ]]
    then
        echo -e "\nAborting."
        exit 1
    fi

    echo   # move to a new line
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

curl -s "http://$IP:$PORT" --output "$OUT_PATH/bundle.zip"
unzip "$OUT_PATH/bundle.zip" -d "$OUT_PATH" > /dev/null
rm "$OUT_PATH/bundle.zip"

# ===== COPY PYCHARM CONSENT VARIABLES =====

mkdir -p "~/.local/share/JetBrains/consentOptions/"
mkdir "~/.java/"

cp "$OUT_PATH/pycharm-consent/accepted" "~/.local/share/JetBrains/consentOptions/"
cp -r "$OUT_PATH/pycharm-consent/.userPrefs/" "~/.java/"

rm -r "$OUT_PATH/pycharm-consent/"

# ===== CREATE VENV =====

python3 -m venv "$OUT_PATH/.venv"
source "$OUT_PATH/.venv/bin/activate"
pip install pygame pyfiglet keyboard
deactivate

# ===== OPEN TERMINAL =====

# Open the HTML files in Firefox
nohup firefox "$OUT_PATH/sujet_1/sujet-1.html" \
              "$OUT_PATH/sujet_2/sujet-2.html" \
              "$OUT_PATH/sujet_3/sujet-3.html" \
              >/dev/null 2>&1 &

# Open the project in PyCharm
nohup pycharm-community "$OUT_PATH" >/dev/null 2>&1 &

# Open terminal and run INIT_CMD
nohup alacritty --hold -e sh -c "$INIT_CMD" >/dev/null 2>&1 &

