#!/usr/bin/env bash
set -euo pipefail

PRACTICALS="ci-scripts/practicals.list"
WHITELIST="ci-scripts/whitelist.include"

DEST_ROOT="ci-imported"
DEST_PRACTICALS="${DEST_ROOT}/practicals"
DEST_SUBJECTS="${DEST_ROOT}/subjects"
DEST_REF="${DEST_ROOT}/ref"

rm -rf "$DEST_ROOT"
mkdir -p "$DEST_PRACTICALS" "$DEST_SUBJECTS" "$DEST_REF"

while read -r name url branch; do
    [[ -z "${name:-}" ]] && continue
    echo "Sync $name from $url ($branch)"
  
    tmp="$(mktemp -d)"
    git clone --depth 1 --branch "$branch" \
       "https://gitlab-ci-token:${CI_JOB_TOKEN}@${url#https://}" \
       "$tmp/repo"
  
    mkdir -p "$DEST_PRACTICALS/$name"
    rsync -a --delete --delete-excluded \
        --include='*/' \
        --include-from="$WHITELIST" \
        --exclude='*' \
        "$tmp/repo/" \
        "$DEST_PRACTICALS/$name/"

    # Copy the subject html
    cp "$tmp/repo/subject.html" "$DEST_SUBJECTS/${name}.html"

    # Copy the ref of the subject
    mkdir -p "$DEST_REF/${name}"
    cp -a "$tmp/repo/ref/." "$DEST_REF/$name/"

    rm -rf "$tmp"
  
done < "${PRACTICALS}"

git add -A
if ! git diff --cached --quiet; then
    git commit -m "Sync practicals"
    git push -o ci.skip origin "HEAD:${CI_COMMIT_BRANCH}"
else
    echo "No changes."
fi
