# BIP Initializer

Generate the Kubernetes manifests your app needs to get started on BIP (Byråets IT-Plattform).

----

[![Build Status](https://dev.azure.com/statisticsnorway/Stratus/_apis/build/status/statisticsnorway.bip-initializer?repoName=statisticsnorway%2Fbip-initializer&branchName=main)](https://dev.azure.com/statisticsnorway/Stratus/_build/latest?definitionId=194&repoName=statisticsnorway%2Fbip-initializer&branchName=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Functionality

This application is developed incrementally, and we will update this documentation as the development progresses.

### Generator

This application generates Kubernetes manifests that are needed for an application to run on BIP. The manifests are created based on some values provided by the user.

Currently, the generator only supports the most basic use case of creating a Flux HelmRelease for a standard backend application. The input values should be provided as a JSON object in a `POST` request to the generate endpoint:

- `/api/v<version>/generate`

See the `docs` info in [Other endpoints](#other-endpoints) to find the API doc for the generator.

#### Supported use cases

- Basic backend app without any GCP "infrastructure", with the following customizations:
  - exposed/unexposed outside the cluster (input parameter `exposed`)
  - with/without Istio end user authentication (input parameter `authentication`)
  - with/without default Kubernetes health probe configuration (input parameter `health_probes`)
  - with/without default metrics endpoint configuration (input parameter `metrics`)

#### Future use cases

Some examples of future use cases are:

- Backend application with GCP infrastructure (Bucket, Cloud SQL, PubSub)
- Basic stand-alone frontend application accessible from outside the cluster
- Frontend application which connects to a backend application within the cluster

### Other endpoints

| Endpoint | Description |
|----------|-------------|
|`/docs` |Endpoint for listing and testing all the endpoints. It's a great help if you're wondering how to format the request to the generator or want to know which values are expected! |
|`/metrics` |Metrics in JSON format |
|`/health/alive`|Returns `200` (OK) if the application is alive (for K8s probes) |
|`/health/ready`|Returns `200` (OK) if the application is ready to accept requests (for K8s probes)  |

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

### Versioning

We use [semantic versioning](https://semver.org/) for the application itself.

The API endpoint for generating manifests is versioned through the URI path, ref. the routing spec for the `generate` method in [app/generate.py](app/generate.py): `/api/v1/generate`.

### Make a new release

Update the release number following [semantic versioning](https://semver.org/). It needs to be updated and kept synchronised in `app/__init__.py` and in `pyproject.toml`, change these both in a single commit. The commit can be in the branch you use to add/edit functionality or in its own branch after the functionality is added. Make a PR containing the commit.

Once the PR is merged, use the [Github release process](https://github.com/statisticsnorway/bip-initializer/releases/new) to release with the same version number. Given the setup in the [build pipeline](azure-pipeline-build.yml) and the [release pipeline](azure-pipeline-release.yml), it's important that the release/tag is created on the merge commit for the PR.

## Run locally

### Run natively

```command
poetry run uvicorn --port 5000 --reload app.main:app
```

### Access locally

With the server running natively (or in [Docker](#Docker)), visit <http://127.0.0.1:5000/docs> to see all available endpoints and test them.

### Run tests

```command
poetry run pytest tests --ignore=tests/resources --junitxml=junit/test-results.xml --cov=app/ --cov-report=xml --cov-report=html
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
