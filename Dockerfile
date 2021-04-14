# Based on the example on https://www.mktr.ai/the-data-scientists-quick-guide-to-dockerfiles-with-examples/
# Under "Dockerfile for Python + poetry + Flask"

###############################################
# Base Image
# ubuntu:20.04 is chosen since it has fewer
# vulnerabilities than images like Debian Buster
###############################################
FROM ubuntu:groovy-20210325 as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3.9 \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/bin/python3.9 /usr/bin/python

###############################################
# Builder Image
###############################################
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install -y  --no-install-recommends \
    ca-certificates \
    curl \
    build-essential \
    python3-distutils \
    python3-apt \
    libpython3.9-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python -

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev

###############################################
# Production Image
###############################################
FROM python-base as production
EXPOSE 5000

# Avoid running as root
RUN useradd --create-home appuser
USER appuser

# Copy the installed dependencies from the Builder Image
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# Copy the app code from the host machine
COPY ./app /app/
COPY ./templates /templates/

# Serve the application with the gunicorn server
# Arguments explanation:
# Spin up 4 workers
# Use the Uvicorn class worker (for asynchronous requests)
# Bind to port 5000
# Log all access to the app
# Serve the app found in the module app.main
CMD [ "gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:5000", "--access-logfile", "-", "app.main:app" ]
