FROM python:3.8-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt \
    && apt-get remove gcc -y \
    && rm -rf /root/.cache/pip
    
RUN mkdir /app
WORKDIR /app

COPY ./app/ .

CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 8000