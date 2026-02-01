#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"
PRACTICALS="ci-scripts/practicals.list"
WHITELIST="ci-scripts/whitelist.include"
DEST_ROOT="ci-imported"
DEST_SUBJECTS="subjects"
DEST_REF="ref"

rm -rf "$DEST_ROOT"
rm -rf "$DEST_SUBJECTS"
rm -rf "$DEST_REF"

mkdir -p "$DEST_ROOT"
mkdir -p "$DEST_SUBJECTS"
mkdir "$DEST_REF"

while read -r name url branch; do
    [[ -z "${name:-}" ]] && continue
    echo "Sync $name from $url ($branch)"
  
    tmp="$(mktemp -d)"
    trap 'rm -rf "$tmp"' EXIT
  
    git clone --depth 1 --branch "$branch" \
       "https://gitlab-ci-token:${CI_JOB_TOKEN}@${url#https://}" \
       "$tmp/repo"
  
    mkdir -p "$DEST_ROOT/$name"
    rsync -a --delete --delete-excluded \
        --include='*/' \
        --include-from="$WHITELIST" \
        --exclude='*' \
        "$tmp/repo/" \
        "$DEST_ROOT/$name/"

    # Copy the subject html
    cp "$tmp/repo/subject.html" "$DEST_SUBJECTS/${name}.html"

    # Copy the ref of the subject
    mkdir "$DEST_SUBJECTS/${name}"
    cp -r "$tmp/repo/ref" "$DEST_SUBJECTS/${name}"

    rm -rf "$tmp"
    trap - EXIT
  
done < "${PRACTICALS}"

