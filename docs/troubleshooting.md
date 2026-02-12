# Troubleshooting

## Common issues

### Global

#### Pygame window won't open

For some reason, on NixOS, when you install pygame using venv, it cannot open a window.
The solution to this is to simply use flakes instead of a venv.
You can find one in the repo of [chip-8](https://gitlab.cri.epita.fr/timothee.le-roux-maertens/chip-8).

### Build

#### fatal: Could not read from remote repository.

This means you do not have the right to clone one of the repositories in `src/manifest.json`.
Make sure that you have the `Developer` role on this repo and that you have set up your SSH key correctly.[^1]

#### nginx: [emerg] still could not bind()

If you get an error like this:
```
fileserver-1  | YYYY/MM/DD HH:MM:SS [notice] 1#1: try again to bind() after 500ms
fileserver-1  | YYYY/MM/DD HH:MM:SS [emerg] 1#1: still could not bind()
fileserver-1  | nginx: [emerg] still could not bind()
```

This means that the nginx Docker Container failed to bind the given ports on `docker/fileserver.conf.template`. All you have to do is modify the used port in:
- `docker/fileserver.conf.template`
- `docker/docker-compose.yml`
- `src/build/bootstrap.sh`

**Warning: the allowed TCP/UDP port range in the PIE is from `42000` to `42999`.**

### Runtime

#### Incorrect password / cannot login

If you tried to log in with:
- username: `epita`
- password: *empty*

and it still doesn't work, it means the sessions were not activated.

This is not directly linked to this repo because it's a problem of the Forge.
Indeed, before each JI, [Lionel](mailto:lionel.brosius@epita.fr) needs to book the session on the Forge, but sometimes either he forgets or it makes a mistake in the dates.

You need to contact Lionel as soon as possible and pray that the Forge answers quickly.

#### Error when trying to download the zip

When you encounter an error when running the curl command, this can come from different factors:
1. Check that the server is running. On the host computer, check the status of the Docker Container with `docker ps`.
2. Make sure you're using curl on the correct IP and port:
    - You can run `ip add` to check the full IP config.
    - Check the port used in `docker/fileserver.conf.template`
    - You can run this curl command instead: `curl -fsSL "https://<ip-host>:42000" > output.txt` and check the content of the output file.
3. Instead of trying to download the `bootstrap.sh` file, you can try to curl the zip manually:
```sh
mkdir ~/ji
cd ~/ji
curl -fsSL "https://<ip-host>:42000" -o "bundle.zip"
unzip "bundle.zip"
./install.sh
```

If the host doesn't work at all, you can try to share the zip file using another method like Google Drive.
Then you just need to unzip it inside `~/ji` and run the `install.sh` file.

#### PyCharm configuration not loaded

It may be possible that after running the installation script on the client computer, PyCharm didn't load the config.

This can happen and it's normal.
In the flake loaded by the client, we copy the folder in `pycharm-config` into `~/.config/JetBrains/PyCharmXXXX.X/`.
However, the folder `PyCharmXXXX.X` can change over the versions of PyCharm.

To fix this issue, check the name of the folder in `~/.config/JetBrains` and make sure it's the same as the one hard-coded in `flake.nix`.
If you see several folders in `~/.config/JetBrains`, this means the flake probably wrote in the wrong folder and you should fix the flake.

#### PyCharm throws an error on launching

As configuration files are loaded manually and not via the PyCharm interface, it can cause some unexpected behaviors.
If PyCharm throws an error when the client computer launches it, it may be because of those configuration files.

First, you need to make sure the files in `~/.config/JetBrains/PyCharmXXXX.X` are in read/write mode.
Indeed, by default, the flake will copy them in read-only mode, which throws an error in PyCharm.

If the files are in read/write mode and you still have an error, try to completely delete the `~/.config/JetBrains` folder and relaunch PyCharm.
If you don't have the error anymore, it means the error was caused by configuration files and they need to be fixed.

If the error persists, try to uninstall and reinstall PyCharm on another version.

[^1]: Go to [cri.epita.fr](https://cri.epita.fr/). Click on your profile, then navigate to `SSH Keys`. Here you can click on the `Help` button. It will show you how to create a new SSH key.
