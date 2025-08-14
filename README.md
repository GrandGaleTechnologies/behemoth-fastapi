# 🚀 Behemoth FastAPI

A powerful, scalable template to kickstart your backend projects. Includes FastAPI with Docker integration, JWT authentication, optional Logfire instrumentation, and PEP-582-based dependency management via Astral's `uv`.

Inspired by [Radoslav Georgiev's Django Structure for Scale lecture](https://youtu.be/yG3ZdxBb1oo?si=D6A9dHyhKb_Kf-J7) and my own experience, this template offers a structured approach to building scalable web applications.

## 📑 Table of Contents

* [✨ Features](#-features)
* [📁 Project Structure](#-project-structure)
* [💡 Getting Started](#-getting-started)
* [🛠️ Using auto-module.py](#️-using-auto-modulepy)
* [🔐 JWT Auth & Security](#-jwt-auth--security)
* [🎗 License](#-license)
* [🚀 Deploy](#-deploy)
* [🤝 Contribute to the Project](#-contribute-to-the-project)
* [📬 Contact](#-contact)

## ✨ Features

* **FastAPI** template with JWT authentication and Alembic migrations.
* **Docker** & **docker-compose** configs for zero-friction container development.
* **Astral `uv`** for dependency installation and script execution (no manual `venv` activation).
* **Logfire auto-instrumentation**: set `LOGFIRE_TOKEN` in your environment and the app will automatically send logs to [Pydantic Logfire](https://logfire.pydantic.dev/docs/).
* **Modular structure** inspired by scaling best practices.
* **Optional `uvloop`** integration for improved asyncio performance (Linux/macOS only).

## 📁 Project Structure

```plaintext
.vscode/
alembic/
app/
  author/
    routes/
      __init__.py
      base.py
    schemas/
      __init__.py
      base.py
      create.py
      edit.py
      response.py
    annotations.py
    apis.py
    crud.py
    exceptions.py
    formatters.py
    models.py
    selectors.py
    services.py
  common/
    annotations.py
    auth.py
    crud.py
    dependencies.py
    exceptions.py
    paginators.py
    schemas.py
    security.py
    types.py
    utils.py
  core/
    database.py
    handlers.py
    settings.py
    tags.py
  external/
    main.py
tests/
.env_sample
.flake8
.gitignore
.pylintrc
.python-version
alembic.ini
auto-module.py
docker-compose.yml
Dockerfile
LICENSE
pyproject.toml
pytest.ini
railway.toml
README.md
requirements.txt
start.sh
uv.lock
```

## 💡 Getting Started

### Prerequisites

* Docker & Docker Compose (optional)
* [`uv`](https://docs.astral.sh/uv/) installed globally

### 1. Clone the repository

```bash
git clone https://github.com/GrandGaleTechnologies/behemoth-fastapi
cd behemoth-fastapi
```

### 2. Install dependencies

#### Using `uv` (recommended)

```bash
# Optional: add uvloop (doesnt work well on windows)
uv add uvloop
uv venv
```

### 3. Environment variables

Copy `.env_sample` to `.env` and set values. If provided, `LOGFIRE_TOKEN` will enable Pydantic Logfire logging. check [this](https://logfire.pydantic.dev/docs/how-to-guides/create-write-tokens/) on how to get your logfire token

### 4. Initialize the database

```bash
# With uv
uv run alembic upgrade head
```

### 5. Start the application

#### Development mode

```bash
uv run fastapi dev
```

#### Production mode

```bash
uv run fastapi run
```

## 🛠️ Using auto-module.py

This script automates creation of new FastAPI modules with a consistent folder layout:

```bash
app/
└── ModuleName/
    ├── routes/__init__.py
    ├── routes/base.py
    ├── schemas/base.py
    ├── schemas/create.py
    ├── schemas/edit.py
    ├── schemas/response.py
    ├── apis.py
    ├── models.py
    ├── services.py
    ├── selectors.py
    ├── exceptions.py
    └── formatters.py
```

### To create a new module:

```bash
uv run auto-module.py
```

Follow the prompts to specify the module name.

## 🔐 JWT Auth & Security

### JWT Authentication

* Implemented in `common/auth.py` and `common/security.py`
* Leverages FastAPI's `Depends` and reusable `get_current_user()` function
* Tokens include expiration and are signed using a secret key in `.env`

### Secure Endpoints

To protect a route:

```python
from common.dependencies import get_current_user

@app.get("/secure-data")
def secure_data(user: User = Depends(get_current_user)):
    return {"message": f"Hello, {user.username}!"}
```

### Auth Flow Overview

1. User logs in via `/login` endpoint → receives JWT access token
2. Frontend stores token (e.g., in localStorage or Authorization header)
3. Token is sent with each protected request
4. Backend validates token and grants access

## Rate Limiting

This project uses Redis-based rate limiting through `fastapi-limiter`. By default, it allows 3 requests per second per endpoint.

### Redis Setup with Docker

1. Add Redis service to your `docker-compose.yml`:
```yaml
// filepath: docker-compose.yml
services:
  # ...existing services...
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - app_network

volumes:
  redis_data:

networks:
  app_network:
    driver: bridge
```

2. Start Redis container:
```powershell
docker-compose up -d redis
```

3. Verify Redis is running:
```powershell
docker-compose exec redis redis-cli ping
```
You should see `PONG` as the response.

### Environment Configuration

Update your `.env` file with the Redis container URL:
```env
REDIS_BROKER_URL=redis://redis:6379/0
```

### Rate Limiting Configuration

Rate limiting is configured in `app/main.py`:
```python
REQ_RATE = 3        # Number of requests allowed
REQ_RATE_TIME = 1   # Time window in seconds
```

This means each endpoint allows 3 requests per second. After exceeding this limit, requests will receive a 429 (Too Many Requests) response.

### Testing Rate Limits

1. **Swagger UI**:
   - Navigate to `http://localhost:8000`
   - Make multiple rapid requests to any endpoint
   - After 3 requests within 1 second, you'll receive a 429 response

2. **Using Docker CLI**:
```powershell
# Make multiple requests quickly
for ($i = 1; $i -le 4; $i++) {
    docker-compose exec api curl http://localhost:8000/health
}
```

### Monitoring Rate Limits

Monitor Redis rate limiting in real-time:
```powershell
docker-compose exec redis redis-cli monitor
```

### Troubleshooting

If Redis connection fails:
1. Check Redis container status:
```powershell
docker-compose ps redis
```

2. View Redis logs:
```powershell
docker-compose logs redis
```

3. Verify Redis network connectivity:
```powershell
docker-compose exec api ping redis
```

4. Check Redis container health:
```powershell
docker inspect -f '{{.State.Health.Status}}' behemoth-fastapi-redis-1
```

5. Restart Redis

## 🎗 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🚀 Deploy

Deploy this template on Railway:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/CtmI_O?referralCode=e77QIa)

## 🤝 Contribute to the Project

Contributions are welcome! Fork the repo, create a branch, and submit a PR. Engage in discussions for ideas and improvements.

## 📬 Contact

* **Name:** GrandGale Technologies
* **Email:** [angobello0@gmail.com](mailto:angobello0@gmail.com)
* **GitHub:** [https://github.com/GrandGaleTechnologies](https://github.com/GrandGaleTechnologies)
* **LinkedIn:** [https://linkedin.com/in/angobello0](https://linkedin.com/in/angobello0)
* **Upwork:** [https://www.upwork.com/freelancers/\~01bb1007bf8311388a](https://www.upwork.com/freelancers/~01bb1007bf8311388a)
* **Instagram:** [https://www.instagram.com/bello\_ango0/](https://www.instagram.com/grandgale_technologies0/)

