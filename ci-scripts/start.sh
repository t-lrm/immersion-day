#!/bin/sh
set -euo pipefail

set -a
source ./env
set +a

require_vars() {
  local v
  for v in "$@"; do
    : "${!v:?Missing $v in .env}"
  done
}

require_vars MOULI_URL MOULI_BRANCH \
    SETUP_PORT SETUP_DST_FOLDER SETUP_DST_FILE \
    SUBJECTS_PORT SUBJECTS_FOLDER \
    ZIP_PORT ZIP_DST_FOLDER ZIP_DST_FILE

ROOT=$(pwd)
OUT="$ROOT/out"

PRACTICALS="$ROOT/practicals.list"
WHITELIST="$ROOT/whitelist.include"

DST_PRACTICALS="$OUT/practicals"
DST_REF="$OUT/ref"
DST_MOULI="$OUT/moulinette"

SRC_CLIENT="$ROOT/client_files"
DST_CLIENT="$OUT/client_files"

SRC_CONFIG_DIR="$ROOT/config_scripts"
SRC_CONFIG_FILES=(variables.sh functions.sh setup.sh)
DST_CONFIG_DIR="$OUT/config"

DST_ZIP_FOLDER="$OUT/zip"

DOCKER_COMPOSE="docker/docker-compose.yml"

rm -rf "$OUT"
mkdir -p "$DST_PRACTICALS" "$DST_SUBJECTS" "$DST_REF" "$DST_MOULI"

# Clone each practical
while read -r name url branch; do
    [[ -z "${name:-}" ]] && continue
    echo "=== Sync $name from $url ($branch)... ==="
  
    tmp="$(mktemp -d)"
    git clone --depth 1 --branch "$branch" "$url" "$tmp/repo"
  
    mkdir -p "$DST_PRACTICALS/$name"
    rsync -a --delete --delete-excluded \
        --include='*/' \
        --include-from="$WHITELIST" \
        --exclude='*' \
        "$tmp/repo/" \
        "$DST_PRACTICALS/$name/"

    # Copy the html subject
    cp "$tmp/repo/subject.html" "$DST_SUBJECTS/${name}.html"

    # Copy the ref of the subject
    mkdir -p "$DST_REF/${name}"
    cp -a "$tmp/repo/ref/." "$DST_REF/$name/"

    rm -rf "$tmp"
  
done < "${PRACTICALS}"

# Clone the moulinette
git clone --depth 1 --branch "$MOULI_BRANCH" "$MOULI_URL" "$DST_MOULI"

# Copy client files into the output folder
cp -r "$SRC_CLIENT" "$DST_CLIENT"

# Build the configuration file and substitute elements
mkdir -p "$DST_CONFIG_DIR"
(
    tmp="$(mktemp)"

    cd "$SRC_CONFIG_DIR"
    cat $SRC_CONFIG_FILES > "$tmp"

    sed \
        -e "s/__IP__/${HOST_IP}/g" \
        -e "s/__PORT_ZIP__/${PORT_ZIP}/g" \
        -e "s/__PORT_SUBJECTS__/${PORT_SUBJECTS}/g" \
        "$tmp" > "$DST_CONFIG_DIR/$DST_CONFIG_FILE"

    chmod +x "$DST_CONFIG_DIR/$DST_CONFIG_FILE"
)

# Build zip
mkdir -p "$ZIP_DST_FOLDER"
zip -r "$DST_ZIP_FOLDER/$DST_ZIP_FILE" $SRC_ZIP_ITEMS

# Run docker container
docker compose -f $DOCKER_COMPOSE up --build --detach
