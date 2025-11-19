# Journées d’immersion

## TODO

### Bugs to fix

- [ ] Pycharm doesn't hide the excluded folders
- [ ] Firefox opens a tab 'Firefox Privacy Notice'

### Improvements to do

- [ ] Update the intro of subject 1 to explain how to run a test suite
- [ ] Check if I can obfuscate the test suites (or create a moulinette ??)
- [ ] Setup an SSH connection on each computer

## Setup instructions

As an organizer, you should:
1. Login to a PIE computer
2. Clone this repository
3. Start the server with `python3 server.py`

Now for each student computer:
1. Boot the computer on any image (you can leave the default one)
2. Login with username `epita` and leave the password empty
3. Open a terminal (`Mod + D`)
4. Run `curl <ip>:42000|sh` (replace `<ip>` with the host ip)
5. Now you should see Pycharm, Firefox and the Tuto appear on the screen
7. You're done!

## Contributions

If you want to contribute to one of the three subjects:
**DO NOT MODIFY IT FROM HERE!!**

Indeed, the folder `sujet_1`, `sujet_2` and `sujet_3` are imported with CI/CD.
So instead, contribute directly on:
- [`mario-python`](https://gitlab.cri.epita.fr/timothee.le-roux-maertens/mario-python) (`sujet_1` & `sujet_2`)
- [`chip-8`](https://gitlab.cri.epita.fr/timothee.le-roux-maertens/chip-8) (`sujet_3`)

If you're a member of the Team JI you should have an access to those repos.
If it's not the case please [contact me](#contact).

Note that you can also find the "ref" on those repos (this can be useful for chip-8).

## Architecture

Here is a detailed explanation of how the CI/CD architecture works with the three repositories:
- `journees-immersion`
- `mario-python`
- `chip-8`

Two CI/CD pipelines are set up for chip-8 and mario-python, exporting the repos
inside `journees-immersion` ensuring the correction files are excluded from the
exports.

A read-only access token is generated for the `journees-immersion` repository.
Using this token, we write a setup script (`setup.sh`) that clones the
repository, and host the script at `ji.baunky.fr`.

Finally, we configure a whitelist so that only EPITA PIE computers can access
`ji.baunky.fr`. Every IP was added manually to only allow Strasbourg computers.

## Setup Gitlab Personnal Access Token (PAT)

Here are the steps to allow a CI/CD to push some commits to repos:
1. Go to `https://gitlab.cri.epita.fr/-/user_settings/personal_access_tokens`
2. Generate a token with the property `write_repository`
3. Go to the section `Settings > CI/CD > Variables` of your repo containing the CI/CD
4. Add a variable with the name you want
5. Now you can use it in your CI/CD

## Setup Gitlab clone token

To create a repository-base token, follow those instructions:
1. Open your GitLab project.
2. Go to Settings → Repository → Deploy tokens.
3. Add a name, expiry date, and select `read_repository`.
4. Now you can use it with `git clone https://<USERNAME>:<TOKEN>@gitlab.cri.epita.fr/<NAMESPACE>/<REPO>.git`

## Contact

You can contact me by email at `timothee.le-roux-maertens@epita.fr` or on Discord (`baunky`).

