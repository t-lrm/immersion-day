#!/bin/sh
set -euo pipefail

CFG="${1:-../manifest.json}"

PRACTICALS="../template/practicals"
MOULINETTE="../template/moulinette"
SUBJECTS="../template/static/subjects"

SRV="../../srv"
ZIP="${SRV}/bundle.zip"

DOCKER_COMPOSE="../../docker/docker-compose.yml"

# Clone each practical
mapfile -t includes < <(jq -r '.practicals.include[]' "$CFG")
jq -c '.practicals.sources[]' "$CFG" | while read -r src; do
  name="$(jq -r '.name' <<<"$src")"
  url="$(jq -r '.url'  <<<"$src")"
  branch="$(jq -r '.branch'  <<<"$src")"

  tmp=$(mktemp -d)

  git clone --depth 1 --branch "$branch" "$url" "$tmp/repo"

  mkdir "${PRACTICALS}/${name}"

  # Copy only whitelisted dirs/files from the cloned repo
  for p in "${includes[@]}"; do
    cp -r "$tmp/repo/${p%/}" "${PRACTICALS}/${name}/"
  done

  # Copy subject page in it's own folder
  cp "$tmp/repo/subject.html" "${SUBJECTS}/${name}.html"

  rm -rf "$tmp"
done


# Clone the moulinette
mouli_url="$(jq -r '.moulinette.url' "$CFG")"
mouli_branch="$(jq -r '.moulinette.branch' "$CFG")"
git clone --depth 1 --branch "$mouli_url" "$mouli_branch" "$MOULINETTE"

# Zip the template folder
rm -f "$ZIP"
(
  cd ../template
  zip -r "$ZIP" .
)

# Start docker
docker compose -f $DOCKER_COMPOSE up --build --detach
