FROM python:3.9-alpine3.15
LABEL org.opencontainers.image.source="https://github.com/samerbahri98/mock-mlops-application"
LABEL maintainer="samer.bahri@edu.bme.hu"
LABEL version="0.1"
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV TZ="Europe/Budapest"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT [ "sh","entrypoint.sh" ]