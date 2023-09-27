FROM python:3.11.5-slim

# Installing poetry to run the project
ENV POETRY_VERSION=1.5.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-env
ENV POETRY_CACHE_DIR=/opt/.cache

RUN apt-get update \
    && apt-get install -y python3.11-dev g++ gcc curl libpq-dev unixodbc unixodbc-dev

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


CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT_TO_EXPOSE} --workers 2 'wsgi:create_app(\"${FLASK_ENV}\")'"]