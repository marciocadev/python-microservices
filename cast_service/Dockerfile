FROM python:3.8-slim

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip
    
RUN mkdir /app
WORKDIR /app

COPY . /app/