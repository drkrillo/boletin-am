FROM python:alpine3.17 AS deps
LABEL maintainer="drk"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY . .
WORKDIR /app
EXPOSE 8000

RUN pip install -r /tmp/requirements.txt
RUN uvicorn main:app --reload