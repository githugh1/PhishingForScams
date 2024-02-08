FROM python:3.11-slim

WORKDIR /home/parser

COPY parser/requirements.txt .
COPY parser/email_parser.py .

RUN mkdir src

COPY q/* src/q/
COPY utils/* src/utils/

RUN pip3 install --no-cache-dir -r requirements.txt