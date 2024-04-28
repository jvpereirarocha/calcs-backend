FROM python:3.11.5-slim

# Installing poetry to run the project
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV POETRY_VERSION=1.5.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-env
ENV POETRY_CACHE_DIR=/opt/.cache

RUN apt-get update \
    && apt-get install -y python3.11-dev g++ gcc curl libpq-dev unixodbc unixodbc-dev \
    && apt-get install -y locales \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv $POETRY_VENV \
    && ${POETRY_VENV}/bin/pip install -U pip setuptools \
    && ${POETRY_VENV}/bin/pip install poetry==${POETRY_VERSION}

# Add poetry to path
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .
ENV FLASK_ENV=${FLASK_ENV:-'production'}
ENV FLASK_APP="wsgi:create_app(\"${FLASK_ENV}}\")"
ENV PORT_TO_EXPOSE=8000

EXPOSE ${PORT_TO_EXPOSE}


CMD ["/bin/bash", "-c", "gunicorn --bind 0.0.0.0:${PORT_TO_EXPOSE} --workers 2 'wsgi:create_app(\"${FLASK_ENV}\")'"]
