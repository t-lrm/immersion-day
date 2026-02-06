# JI

## Overview

This repository builds and distributes the practicals used during "Journées d'Immersion" (it may also be used for "Stages de seconde").
If you want to know more about how this repo works, check out [documentation][documentation] where the operation of the repo is detailed.

## Setup

### Host

As an organizer, you should:
1. clone this repo using SSH,
2. run `./src/build/build.sh`,
3. wait until you see Docker container is running.

### Client

Now for each client computer:
1. boot the computer on any image (you can leave the default one),
2. login with:
    - username: `epita`
    - password: *(leave empty)*
3. then run this command: `curl <host ip>:42000 | bash`.[^1]

Once done, you should see a popup in fullscreen with a welcome message.
If you want to exit fullscreen, you can press `mod + f`.
You should also see Firefox and PyCharm opened.

## Configuration

The main configuration file is `src/manifest.json`. It determines:
- which practical repositories are cloned,
- which folders are copied into the final bundle,
- how the moulinette is configured.

## Contributions

These are the steps to contribute to this repo:
1. Create a branch with this format: `<your-name>/<feature-or-fix-name>`.
2. Make your changes on that branch and push your commits.
3. Open a merge request targeting main.
4. Your changes will be reviewed and merged if everything looks good.

If you want to create a new practical, see [practicals][practicals] for the expected repository structure and setup.

## Troubleshooting

If you encounter any errors or unexpected behaviour, read [troubleshooting][troubleshooting].
It may give you some clue about your issue.

## Contact

If you have any question, you can contact me via:
- Email: `timothee.le-roux-maertens@epita.fr`
- Discord: `baunky`

[^1]: *To show the host ip you can either check the i3 status bar or run `hostname -I`.*

[documentation]: ./docs/documentation.md
[practicals]: ./docs/practicals.md
[troubleshooting]: ./docs/troubleshooting.md

