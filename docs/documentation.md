# Documentation

## Overview

This file describes in detail how the repo works.

## Introduction

This repo was originally created for "Journées d'Immersion" (JI) at EPITA.
Its goal is to:
- set up the computer so that students don't have to open the practicals manually,
- offer several working practicals that are intuitive to use,
- simplify as much as possible the setup of the computer during those JI.

To meet those goals, we've decided to use a client/server architecture.

## Server

We could've used a public server with a domain name, but it had three major problems:
1. it costs some money,
2. the practicals would become public (we don't want to share any of the subjects, as some schools already stole some of our practicals),
3. it's hard to manage and a bit overkill in our case.

So we chose to make the server local and to run it only when needed, so it's restricted to the local network of EPITA.

This server is managed by [Docker](https://www.docker.com/) using [nginx](https://nginx.org/).

The goal of this server is to serve a zip file that will contain everything needed by the client:
- configuration scripts (welcome message, software installation...)
- practicals (subject, Python files, test suites...)
- Python dependencies (moulinette and other packages)

We also host a bootstrap which helps us download the script, extract it, and run the `install.sh` file.
This way, we have only one command to run on each computer.

## Build

The goal of the build is to generate the zip file that will contain everything the client needs.
That is:
- each practical (including the subject),
- the moulinette,
- the PyCharm configuration,
- the system configuration (i.e. bashrc),
- the welcome message,
- some installation scripts.

To do so, we'll first clone every repo (practicals + moulinette), and filter the content to get only some specific folders.
You can change this list in `src/manifest.json`.

For each practical, we'll copy the `subject.html` file and paste it inside `src/template/static/subjects`.

Then we need to do a little trick with the PyCharm configuration.
We need to generate the `recentProjects.xml` file, so that the client doesn't have to find the practical location on its own. To do so, we use the `src/build/populate_projects.py` file.

Once everything is done, we zip the entire `src/template` folder to serve it inside `srv/`.

We also serve the `src/build/bootstrap.sh` script to simplify the download of the zip.

Finally, we start Docker Compose in detached mode.
