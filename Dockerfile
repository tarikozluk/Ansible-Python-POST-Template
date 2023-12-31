# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /ansible-posting-requests

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "api_main.py"]
