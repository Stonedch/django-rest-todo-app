FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./django_rest_todo_app/Pipfile /django_rest_todo_app/Pipfile.lock ./backend/

RUN pip install --upgrade pip
RUN pip install pipenv gunicorn

RUN cd ./backend/ && pipenv install --system --deploy --ignore-pipfile

COPY ./docker/ ./docker/
COPY ./django_rest_todo_app/ ./backend/
