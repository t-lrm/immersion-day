#!/bin/sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

CFG_DEFAULT="${REPO_ROOT}/src/manifest.json"

PRACTICALS="${REPO_ROOT}/src/template/practicals"
MOULINETTE="${REPO_ROOT}/src/template/moulinette"
SUBJECTS="${REPO_ROOT}/src/template/static/subjects"

SRV="${REPO_ROOT}/srv"
ZIP="${SRV}/bundle.zip"

DOCKER_COMPOSE="${REPO_ROOT}/docker/docker-compose.yml"


