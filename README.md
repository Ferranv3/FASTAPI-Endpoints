# FAST API Endpoints

![Build Status](https://github.com/Ferranv3/FASTAPI-Endpoints/actions/workflows/ci.yml/badge.svg?branch=main)

This project exposes a small API using **FastAPI** backed by a SQLite database. It can be started quickly using Docker.

The source now follows a lightweight hexagonal architecture:

- **routers** act as the entry points.
- **services** contain business logic and validations.
- **repositories** perform database access.

## Installation

### Prerequisites
Make sure you have `docker` and `docker-compose` installed on your machine.

### Run
```bash
docker-compose up --build --remove-orphans
```
The command above initializes the database and starts the API on port `8000`.

To stop and remove the containers run:
```bash
docker-compose down --rmi all
```

## Endpoints
The API provides the following routes:

- `GET /` - basic health check returning a simple message.
- `GET /users` - list users filtered by `email` or `id`.
- `GET /products` - list products filtered by `name` or `id`.
- `GET /orders` - list orders filtered by `user_id` or `id`.
- `GET /orderItems` - list order items filtered by `order_id` or `id`.
- `GET /categories` - list categories filtered by `name` or `id`.

All list endpoints require the query parameter `language` which can be `es` or `en`.

