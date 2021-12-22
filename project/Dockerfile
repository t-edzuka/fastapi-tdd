FROM python:3.9.9-slim-buster
# RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean \
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .