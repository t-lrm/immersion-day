#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

MOD="Win"

shortcuts_message() {
  cat <<EOF
Voici le kit de survie pour vous familiariser avec votre nouvel environnement :

  $MOD + D           : Chercher un programme
  $MOD + Shift + Q   : Fermer une fenêtre
  $MOD + [number]    : Accéder au workspace n°[number]
  $MOD + Entrée      : Ouvrir un nouveau terminal

Commandes shell utiles (à faire dans un terminal) :
  ls                 : Lister les fichiers du dossier actuel
  cd [dir]           : Se déplacer dans le dossier [dir]
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

