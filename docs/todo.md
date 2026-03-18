# Todo

## Fixes

- [ ] Update every practical subject
- [ ] Add more detailed failure output when a function fails.
- [ ] Provide a file where students can see the output of their function, not just pass/fail.
- [ ] Prevent Firefox from opening the "Firefox Privacy Notice" tab.
- [ ] Detect infinite loops and fail tests with a clear message.

## Features

- [X] Disable sleep mode in the config script.
- [ ] Create a tutorial on how to use PyCharm (how to run test suites, how to run your code...)
- [ ] Create an index.html that lists the available subjects instead of the default Firefox file explorer.
- [ ] Push test suite results back to the server for statistics.
    On each run of the moulinette, we store the json report in a folder common to each practical.
    Then we also create a command that zips this folder and sends it to the server (this command will be run by organizers at then end of the JI).
    The server takes all the zip, extracts them, rename the files with the ip of the client computer and place them in a common folder.
    Then we set a simple script to run the statistics on the computer.
    We also would like to export the stats into a log file to see the evolution of the test suite percentages (we don't want to store every test file as it would take too much space).
- [ ] Add a room map indicating which PCs should (and should not) be booted for the OCR presentation.
