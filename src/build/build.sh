#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

CFG="${1:-$CFG_DEFAULT}"

# Clean the destination folders
"${REPO_ROOT}/src/build/clean.sh"

# Clone each practical
mapfile -t includes < <(jq -r '.practicals.include[]' "$CFG")
jq -c '.practicals.sources[]' "$CFG" | while read -r src; do
  name="$(jq -r '.name' <<<"$src")"
  url="$(jq -r '.url'  <<<"$src")"
  branch="$(jq -r '.branch'  <<<"$src")"

  tmp=$(mktemp -d)

  echo "Cloning ${url} (${branch})..."
  git clone --depth 1 --branch "$branch" "$url" "$tmp/repo"

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
  git clone --depth 1 --branch "$branch" "$url" "$tmp/repo"

  cp -r "$tmp/repo"/* "$MOULINETTE"
)

# Populate the recent projects config file of Pycharm
python3 "${REPO_ROOT}/src/build/populate_projects.py" \
  --manifest "$CFG" \
  --out "${PYCHARM_CONFIG}/options/recentProjects.xml" \
  --projects-root "$USER_ROOT/practicals"

# Zip the template folder
mkdir -p "$SRV"
(
  cd "${REPO_ROOT}/src/template"
  zip --recurse-paths --quiet "$ZIP" .
)

# Copy src/build/bootstrap.sh into srv/bootstrap.sh and replace IP
cp "${REPO_ROOT}/src/build/bootstrap.sh" "${REPO_ROOT}/srv/bootstrap.sh"
IP="$(hostname -I | awk '{print $1}')"
sed -i "s|__IP__|$IP|g" "${REPO_ROOT}/srv/bootstrap.sh"

# Start docker
docker compose -f $DOCKER_COMPOSE up --build --detach
