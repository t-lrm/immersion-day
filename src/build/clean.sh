#!/bin/sh
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

rm -rf "${PRACTICALS}"/*
rm -rf "${MOULINETTE}"/*
rm -rf "${SUBJECTS}"/*
rm -rf "${SRV}"/*
