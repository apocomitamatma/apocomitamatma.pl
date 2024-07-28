# syntax = docker/dockerfile:1.4

FROM python:3.11-slim AS builder
WORKDIR /app
COPY ./ ./
RUN pip install -r requirements.lock

CMD ["fastapi", "run"]