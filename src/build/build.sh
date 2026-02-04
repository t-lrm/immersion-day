#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

CFG="${1:-$CFG_DEFAULT}"

# Clean the destination folders
./"$(dirname "${BASH_SOURCE[0]}")/clean.sh"

# Clone each practical
mapfile -t includes < <(jq -r '.practicals.include[]' "$CFG")
jq -c '.practicals.sources[]' "$CFG" | while read -r src; do
  name="$(jq -r '.name' <<<"$src")"
  url="$(jq -r '.url'  <<<"$src")"
  branch="$(jq -r '.branch'  <<<"$src")"

  tmp=$(mktemp -d)

  echo "Cloning ${url} (${branch})..."
  git clone --depth 1 --branch "$branch" "$url" "$tmp/repo" 2>/dev/null

  mkdir "${PRACTICALS}/${name}"

  # Copy only whitelisted dirs/files from the cloned repo
  for p in "${includes[@]}"; do
    src="$tmp/repo/${p%/}"
    dst="${PRACTICALS}/${name}/"

    if [[ -d "$src" ]]; then
      cp -r "$src" "$dst"
    else
      echo "Skipping missing directory: $src" >&2
    fi
  done

  # Copy subject page in it's own folder
  cp "$tmp/repo/subject.html" "${SUBJECTS}/${name}.html"

  rm -rf "$tmp"
done


# Clone the moulinette
url="$(jq -r '.moulinette.url' "$CFG")"
branch="$(jq -r '.moulinette.branch' "$CFG")"
(
  tmp=$(mktemp -d)

  echo "Cloning ${url} (${branch})..."
  git clone --depth 1 --branch "$branch" "$url" "$tmp/repo" 2>/dev/null

  cp -r "$tmp/repo" "$MOULINETTE"
)

# Zip the template folder
mkdir -p "$SRV"
(
  cd "${REPO_ROOT}/src/template"
  zip --recurse-paths --quiet "$ZIP" .
)

# Start docker
docker compose -f $DOCKER_COMPOSE up --build
