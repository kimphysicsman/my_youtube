FROM python:3.10.0-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /usr/src/app/

WORKDIR /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app/