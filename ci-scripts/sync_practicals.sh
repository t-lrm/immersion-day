#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"
DEST_ROOT="ci-imported"
DEST_SUBJECTS="subjects"
BRANCH="main"

rm -rf "$DEST_ROOT"
mkdir -p "$DEST_ROOT"

while read -r name url; do
    [[ -z "${name:-}" ]] && continue
    echo "Sync $name from $url ($BRANCH)"
  
    tmp="$(mktemp -d)"
    trap 'rm -rf "$tmp"' RETURN
  
    git clone --depth 1 --branch "$BRANCH" \
       "https://gitlab-ci-token:${CI_JOB_TOKEN}@${url#https://}" \
       "$tmp/repo"
  
    mkdir -p "$DEST_ROOT/$name"
    rsync -a --delete --delete-excluded \
        --include='*/' \
        --include-from=whitelist.include \
        --exclude='*' \
        ./  "${DIR_DST}/"
  
done < "${ROOT}/practicals.list"

