# bip-initializer

Generate everything your app needs to get started on BIP

----

[![Build Status](https://dev.azure.com/statisticsnorway/Stratus/_apis/build/status/statisticsnorway.bip-initializer?repoName=statisticsnorway%2Fbip-initializer&branchName=refs%2Fpull%2F9%2Fmerge)](https://dev.azure.com/statisticsnorway/Stratus/_build/latest?definitionId=194&repoName=statisticsnorway%2Fbip-initializer&branchName=refs%2Fpull%2F9%2Fmerge)
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

### Code format

This project makes use of the opinionated code formatting tool [Black](https://github.com/psf/black). This ensures consistency in code formatting across the project and avoids unnecessary flame wars over style.

It is recommended to run black automatically every time you change files. This is supported by use of the [pre-commit](https://pre-commit.com/) tool. To set it up, just run `pre-commit install` the first time you set up the project.

## Docker

### Build

```command
docker build . -f Dockerfile -t bip-initializer
```

### Run

```command
docker run -p 5000:5000 bip-initializer:latest
```

## Run tests

```command
poetry run pytest tests --ignore=tests/resources --junitxml=junit/test-results.xml --cov=app/ --cov-report=xml --cov-report=html
```

## Access locally

With the server running natively (or in [Docker](#Docker)), visit <http://127.0.0.1:5000/docs> to see all available endpoints.
