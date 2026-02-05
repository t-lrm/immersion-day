#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
USER_ROOT="$HOME/ji" # folder where the client has extracted the zip

CFG_DEFAULT="${REPO_ROOT}/src/manifest.json"

PRACTICALS="${REPO_ROOT}/src/template/practicals"
MOULINETTE="${REPO_ROOT}/src/template/moulinette"
SUBJECTS="${REPO_ROOT}/src/template/static/subjects"
PYCHARM_CONFIG="${REPO_ROOT}/src/template/pycharm-config"

SRV="${REPO_ROOT}/srv"
ZIP="${SRV}/bundle.zip"

DOCKER_COMPOSE="${REPO_ROOT}/docker/docker-compose.yml"


