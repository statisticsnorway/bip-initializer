# bip-initializer

Generate everything your app needs to get started on BIP

----

[![Build Status](https://dev.azure.com/statisticsnorway/Stratus/_apis/build/status/statisticsnorway.bip-initializer?repoName=statisticsnorway%2Fbip-initializer&branchName=main)](https://dev.azure.com/statisticsnorway/Stratus/_build/latest?definitionId=194&repoName=statisticsnorway%2Fbip-initializer&branchName=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Contribute

### Requirements

Requirement        | Installation | Version  | Description
------------------ | ------------ | -------- | ----------------
Python             | Pre-installed on most systems | >2.7 (Poetry will take care of rest)     | Interpreter
Docker (optional!) | <https://docs.docker.com/get-docker/> | Recent | Builds images and runs containers
Poetry             | [See the docs here](https://python-poetry.org/docs/#osx-linux-bashonwindows-install-instructions) | ^1.1     | Version Management for Python projects

After Poetry is installed, install all other requirements and set up the project by running:

```command
poetry shell
poetry install
pre-commit install
```

> :information_source: Poetry shows a warning running on Mac. This is because the alias `python` on Mac points to Python 2.7 :facepalm:. You may see a warning like the following:
>
> ```command
> Python 2.7 will no longer be supported in the next feature release of Poetry (1.2).
> You should consider updating your Python version to a supported one.
> ```
>
> To fix this, change the line `#!/usr/bin/env python` in `~/.poetry/bin/poetry` to `#!/usr/bin/env python3`

### Add a new dependency

To add a new dependency to the project, just run `poetry add <package_name>`. This will install the package from the PyPi servers into the virtual environment, and record the installed version in `pyproject.toml` and in `poetry.lock`. When `poetry install` is run, the *exact* versions recorded in `poetry.lock` will be installed.

It is also possible to manually edit `pyproject.toml` to change, add or remove dependencies. Be aware that this won't have any effect on running `poetry install` unless you first run `poetry update` to apply the changes to your local environment and `poetry.lock`.

### Code format

This project makes use of the opinionated code formatting tool [Black](https://github.com/psf/black). This ensures consistency in code formatting across the project and avoids unnecessary flame wars over style.

It is recommended to run black automatically every time you change files. This is supported by use of the [pre-commit](https://pre-commit.com/) tool. To set it up, just run `pre-commit install` the first time you set up the project.

## Run locally

### Run natively

```command
poetry run uvicorn --port 5000 --reload app.main:app
```

### Access locally

With the server running natively (or in [Docker](#Docker)), visit <http://127.0.0.1:5000/docs> to see all available endpoints.

### Run tests

```command
poetry run pytest
```

### Docker

#### Build

```command
docker build . -f Dockerfile -t bip-initializer
```

#### Run

```command
docker run -p 5000:5000 bip-initializer:latest
```
