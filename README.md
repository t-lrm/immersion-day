# JI

## Overview

This repository builds and distributes the practicals used during "Journées d'Immersion" (JI).
Note that it may also be used for "Stages de seconde".
If you want to know more about how this repo works, check out [documentation][documentation], where the operation of the repo is detailed.

## Setup

This repo uses a host/client system to set up the computers and ensure the organizer has as little commands to type as possible.
To make this work, one of the organizer needs to boot their session and follow the [host instructions](#host)

First you need to run `nix develop` at the root of the repo to install build dependencies.

### Host

As an organizer, you should:
1. clone this repo _(via SSH, not HTTPS, of course)_,
2. run `./src/build/build.sh`,
3. wait until you see that the Docker Container is running.

### Client

Now, for each client computer:
1. boot the computer with any image (you can leave the default one),
2. log in with:
    - username: `epita`
    - password: *(leave empty)*
3. then run this command: `curl <host-ip>:42000 | bash`.[^1]

Once done, you should see a pop-up in full screen with a welcome message.
If you want to exit fullscreen, you can press `Mod + F`.
You should also see Firefox and PyCharm opened.

**Warnings:**
1. The bootstrap script will use `~/ji` as the default folder.
If you want to test the client script on you personal computer and already have this folder, it could erase some of it's content.
2. It may also overwrite your PyCharm configuration files in `~/.config/JetBrains/PyCharmXXXX.X`.
Make sure to back it up or log in to link the configuration to your account.

## Configuration

The main configuration file is `src/manifest.json`. It determines:
- which practical repositories are cloned,
- which folders are copied into the final bundle,
- how the moulinette is configured.

## Contributions

Steps to contribute to this repo:
1. Create a branch with this format: `<your-name>/<feature-or-fix-name>`.
2. Make your changes on that branch, then push your commits.
3. Don't forget to update the documentation!
4. Open a merge request targeting `main`.
5. Your changes will be reviewed and merged if everything looks good.

If you want to create a new practical, see [practicals][practicals] for the expected repository structure and setup.

## Troubleshooting

If you encounter any errors or unexpected behavior, read [troubleshooting][troubleshooting].
It may give you some clues about your issue.

## Todo

Check [todo][todo].

## Contact

If you have any questions, you can contact me via:
- Email: `timothee.le-roux-maertens@epita.fr`
- Discord: `baunky`

[^1]: *To display the host **local** IP, you can either check the i3 status bar or run `hostname -I`.*

[documentation]: ./docs/documentation.md
[practicals]: ./docs/practicals.md
[troubleshooting]: ./docs/troubleshooting.md
[todo]: ./docs/todo.md
