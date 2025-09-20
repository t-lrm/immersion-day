# Journées d’immersion

## Correction

The correction of the exercices are here:
- https://gitlab.cri.epita.fr/timothee.le-roux-maertens/chip-8
- https://gitlab.cri.epita.fr/timothee.le-roux-maertens/mario-python

If you're a member of the Team JI you should have an access to those repos.
If it's not the case please [contact me](#contact).

## Architecture

We create three private repositories:
- `chip-8`
- `mario-python`
- `journees-immersion`

Two CI/CD pipelines are set up for chip-8 and mario-python, exporting the repos inside `journees-immersion` ensuring
the correction files are excluded from the exports.

A read-only access token is generated for the `journees-immersion` repository. Using this token, we write a setup
script (`setup.sh`) that clones the repository, and host the script at `ji.baunky.fr`.

Finally, we configure a whitelist so that only EPITA PIE computers can access `ji.baunky.fr`.

## Setup Gitlab Personnal Access Token (PAT)

Here are the steps to allow a CI/CD to push some commits to repos:
1. Go to `https://gitlab.cri.epita.fr/-/user_settings/personal_access_tokens`
2. Generate a token with the property `write_repository`
3. Go to the section `Settings > CI/CD > Variables` of your repo containing the CI/CD
4. Add a variable with the name you want
5. Now you can use it in your CI/CD

## Setup Gitlab clone token

TODO

## Contact

You can contact me by email at `timothee.le-roux-maertens@epita.fr` or on Discord (`baunky`).

