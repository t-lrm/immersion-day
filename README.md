# Journées d’immersion

## Architecture

We create two private repos:
- `chip-8`
- `mario-python`

We create another private repos:
- `journees-immersion`

We create two workflows that exports `chip-8` and `mario-python` removing the correction files.

We generate a read-only access token to the repo `journees-immersion`.

We create a setup script to clone the repo `journees-immersion` using the secret token.

We host this script and setup an IP to whitelist computer from the PIE.

We destroy the file and clear the history when done.

## Setup Github Token

1. Go to Settings → Developer settings → Personal access tokens → Fine-grained tokens
2. Click Generate new token.
3. Give it a name (and a description if you want)
4. Select the repositories you want
5. Add a `Content` permission with `Read-only`

## Setup Gitlab Token

Here are the steps to allow a CI/CD to push some commits to repos:
1. Go to `https://gitlab.cri.epita.fr/-/user_settings/personal_access_tokens`
2. Generate a token with the property `write_repository`

3. Go to the section `Settings > CI/CD > Variables` of your repo containing the CI/CD
4. Add a variable with the name you want
5. Now you can use it in your CI/CD

