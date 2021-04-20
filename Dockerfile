FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN apt-get update && apt-get -y install cron
COPY update-cron /etc/cron.d/update-cron
RUN chmod 0644 /etc/cron.d/update-cron
RUN crontab /etc/cron.d/update-cron
RUN touch /var/log/cron.log

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.3

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /app/

ENV MODULE_NAME="src.api.main"
ENV APP_MODULE="src.api.main:app"

ENV DB_URL='sqlite:////app/information.db'
ENV MAILGUN_API_KEY='YOUR KEY FOR EMAIL'
ENV DOMAIN_NAME='YOUR DOMAIN FOR EMAIL'


RUN python src/api/models.py
RUN python src/utils/link_parser.py wiki_links.txt
