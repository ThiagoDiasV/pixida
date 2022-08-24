FROM python:3.9-slim-bullseye AS django-dev

ENV PYTHONUNBUFFERED 1

COPY . /opt/app
RUN apt update && \
    apt-get install -y --no-install-recommends \
    gcc \
    curl \
    libcurl4-openssl-dev \
    libssl-dev \
    git && \
    pip install -U pip \
    && pip install pipenv \
    && cd /opt/app \
    # using virtual environment in this context is unnecessary, then
    # installing all packages globally.
    && pip install -r requirements-dev.txt

RUN cp /opt/app/docker/django-entrypoint.sh /docker-entrypoint.sh \
    && chmod +x /docker-entrypoint.sh

EXPOSE 8000

WORKDIR /opt/app/src

ENTRYPOINT [ "/docker-entrypoint.sh" ]
