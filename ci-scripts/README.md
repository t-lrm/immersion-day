# ci-scripts

## Overview

This folder contains the script used by the Gitlab CI/CD to imports every practicals.

## Import a practical

Each practical must have this file architecture:
```sh
.
├── skeleton/
├── ref/
├── tests/
├── other/
├── README.md
├── requirements.txt
└── subject.html
```

Considering this file architrecture, we will import those folders:
- `skeleton`
- `test`
- `other`

And the file `subject.html` will be imported inside the `subjects` folder.
