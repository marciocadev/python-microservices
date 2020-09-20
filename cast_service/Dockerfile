FROM python:3.8-slim AS base

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt \
    && apt-get remove gcc -y \
    && rm -rf /root/.cache/pip
    
RUN mkdir /app
WORKDIR /app

COPY ./app/ /app/

########## DEBUGGER ##########
FROM base AS debug

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements-dev.txt requirements.txt

RUN pip install -r requirements.txt

CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

########## PRODUCTION ##########

FROM base AS prod

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN adduser --disabled-password appuser \
    && chown -R appuser /src
    
USER appuser

CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 8000