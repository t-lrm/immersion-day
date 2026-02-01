#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"
PRACTICALS="ci-scripts/practicals.list"
WHITELIST="ci-scripts/whitelist.include"
DEST_ROOT="ci-imported"
DEST_SUBJECTS="subjects"
BRANCH="tlrm/rework" #FIXME: change to main when merging

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
        --include-from="$WHITELIST" \
        --exclude='*' \
        ./ "$DEST_ROOT/$name" 
  
done < "${PRACTICALS}"

