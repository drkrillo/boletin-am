FROM python:3.11.4-alpine3.18
COPY ./requirements.txt /tmp/requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . .
WORKDIR /app
EXPOSE 8000

RUN pip install -r /tmp/requirements.txt
RUN python task.py