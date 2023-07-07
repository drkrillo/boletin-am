FROM python:3.11.4-alpine3.18
LABEL maintainer="drk"
COPY ./requirements.txt /tmp/requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . .
WORKDIR /app
EXPOSE 8000

RUN pip install -r /tmp/requirements.txt
CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000