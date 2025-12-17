# Journées d’immersion

## Setup instructions

As an organizer, you should:
1. Login to a PIE computer
2. Clone this repository _(in SSH not in HTTPS of course)_
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

Then, when you clone this repo and run the server, two ports are opened:
- `42000: setup.sh`
- `42001: bundle.zip`

When the client will download and execute the setup script, this setup will take
care of downloading, extracting and setting up the folder architecture.

## TODO

### Bugs to fix

- [ ] Update the intro of subject 1 to explain how to run a test suite (confirm with Lionel if we can use markdown instead of the weird HTML)
- [X] Update subject 1: avoid using prints in function `give_grade` as it's confusing for the students
- [ ] It could be greate to have more verbose when a function fails instead of a simples message like "function failed"
- [ ] It could be great to add a file where students can see the result of their function. Now, they only see if the test passed or not.
- [ ] Pycharm doesn't hide the excluded folders
- [ ] Firefox opens a tab 'Firefox Privacy Notice'

### Improvements to do

- [ ] Check if I can obfuscate the test suites (or create a moulinette ??)
- [ ] Setup an SSH connection on each computer
- [ ] Merge the repos `chip-8` and `mario-python` into `ji`
- [ ] Add a map of the room to show which PC should be booted and tell that a pc should not be booted so that it can be used for the OCR presentation

## Contact

You can contact me by email at `timothee.le-roux-maertens@epita.fr` or on Discord (`baunky`).

