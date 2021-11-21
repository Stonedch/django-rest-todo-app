# Pull official base image
FROM python:3.8-alpine

# Set work directory
WORKDIR /usr/src/app

# Copy project
COPY . .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Install pipenv
RUN pip install pipenv

# Install dependencies
RUN pipenv install --system --deploy --ignore-pipfile
