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

