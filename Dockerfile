FROM python:3.11-slim

#Install sqlite3 and dependencies
RUN apt-get update && apt-get install -y sqlite3 && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/data && chmod 777 /app/data

EXPOSE 8000
