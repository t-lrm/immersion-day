# Documentation

## Overview

This file describes in detail how the repo works.

## Introduction

This repo was originally created for "Journées d'Immersion" (JI) at EPITA.
Its goals are to:
- set up the computer so that high school students don't have to open the practicals manually,
- offer several working practicals that are intuitive to use,
- reduce as much as possible the number of commands to type on each computer during setup.

To meet those goals, we've decided to use a local client/server architecture:
- the server will be represented by an EPITA student session,
- the client corresponds to sessions logged in as `epita`.

## Server

We could've used a public server with a domain name, but it had three major problems:
1. it costs money,
2. the practicals would become public (we don't want to share any of the subjects, as some practicals were stolen by the past),
3. it's hard to maintain and a bit overkill in our case.

So we chose to make the server local and to run it only when needed, so it's restricted to EPITA's local network.

This server is managed by [Docker](https://www.docker.com/) using [nginx](https://nginx.org/).
You don't need to know much about those tools.
The only thing you need are these commands:
- `docker ps [--all]` to list containers,
- `docker compose -f <path-to-docker-compose.yml> up --build` to build and start the Docker Compose,
- `docker compose stop <container-hash>` to stop a container.
- `docker kill <container-hash>` to kill a container.

The goal of this server is to serve a zip file that will contain everything needed by the client:
- configuration scripts (welcome message, software installation...)
- practicals (subject, Python files, test suites...)
- Python dependencies (moulinette and other external packages like `pygame` for example)

We also serve a [bootstrap script][bootstrap] which helps us download the script, extract it, and run the [install.sh][install] file.
This way, we have only one command to run on each computer (this makes the setup pretty simple).

## Build scripts

The goal of the [build script][build] is to generate the zip file that will contain everything the client needs.
That is:
- each practical (including the subject),
- the moulinette,
- the PyCharm configuration,
- the system configuration (i.e. bashrc),
- the welcome message,
- some installation scripts.

To do so, we'll first clone every repo (practicals + moulinette) in a temporary folder, and copy the content of this folder, applying a filter to get only needed folders (and mainly to exclude the `ref` folder).
You can change what's cloned and the filter in [manifest.json][manifest].

When a practical is cloned, we copy the `subject.html` file and paste it inside [`src/template/static/subjects`][subjects].

Concerning the PyCharm configuration, we wanted to show the list of practicals in the "Recent Projects" section of PyCharm.
We also needed to set up the Python interpreter and some other settings.
To do so, we simply copy a list of XML configuration files and paste it inside the PyCharm default configuration folder (you can check the [populate_projects.py][populate_projects] Python script and the [pycharm-config][pycharm-config] folder).

Once everything is complete, we zip the entire `src/template` folder to serve it inside `srv/`.
We also serve the `src/build/bootstrap.sh` script to simplify the download of the zip.

Finally, we start Docker Compose in detached mode.

[bootstrap]: ../src/build/bootstrap.sh
[install]: ../src/template/install.sh
[build]: ../src/build/build.sh
[manifest]: ../src/manifest.json
[subjects]: ../src/template/static/subjects
[populate_projects]: ../src/build/populate_projects.py
[pycharm-config]: ../src/template/pycharm-config
