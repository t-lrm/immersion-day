#!/usr/bin/env bash
set -e


echo "This will delete:"
echo "  - ~/.config/JetBrains"
echo "  - ~/ji"
echo
echo "And run: nix profile remove ji"
echo

read -r -p "Continue? [y/N] " ans
case "$ans" in
  y|Y|yes|YES) ;;
  *) echo "Aborted."; exit 1 ;;
esac

rm -rf ~/.config/JetBrains ~/ji
nix profile remove ji >/dev/null 2>&1

