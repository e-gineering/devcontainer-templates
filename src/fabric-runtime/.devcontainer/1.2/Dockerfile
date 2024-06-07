# Bullseye contains JDK 11 in its apt repos
FROM mcr.microsoft.com/devcontainers/python:1-3.10-bullseye

RUN apt-get update && \
  apt-get install -y \
  bash-completion \
  openjdk-11-jdk-headless

COPY requirements.txt /tmp/requirements.txt
RUN pip install --requirement /tmp/requirements.txt
