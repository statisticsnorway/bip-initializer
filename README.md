# bip-initializer

Generate everything your app needs to get started on BIP

## Contribute

### Requirements

Requirement | Installation | Version  | Description
----------- | ------------ | -------- | ----------------
Python      | Pre-installed on most systems | Any (Poetry will handle the version used in project virtual env)     | Interpreter
Docker      | <https://docs.docker.com/get-docker/> | Recent | Builds images and runs containers
Poetry      | [See the docs here](https://python-poetry.org/docs/#osx-linux-bashonwindows-install-instructions) | ^1.1     | Version Management for Python projects

To install all other requirements, run

```command
poetry shell
poetry install
```

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
poetry run pytest
```

## Access locally

With the server running natively (or in [Docker](#Docker)), visit <http://127.0.0.1:5000/docs> to see all available endpoints.
