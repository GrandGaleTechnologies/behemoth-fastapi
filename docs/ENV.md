# Environment Variables Guide

This guide explains what each environment variable does, what value to put, and how to obtain it.

## Core

- **DEBUG**
  - What to put: `true` for development, `false` for production
  - Purpose: Controls debug mode, enables/disables Swagger UI docs, and sets Logfire environment
  - How to get: Set to `true` during development, `false` in production

## Database

- **POSTGRES_DATABASE_URL**
  - What to put: `postgresql+asyncpg://username:password@host:port/database_name`
  - Purpose: PostgreSQL database connection URL for the application
  - How to get: 
    - **Local Development**: `postgresql+asyncpg://postgres:password@localhost:5432/behemoth_db`
    - **Docker Compose**: `postgresql+asyncpg://behemoth:backend@behemoth_db:5432/behemoth_db`
    - **Production**: Get from your database provider (Railway, AWS RDS, etc.)
    - **Format**: `postgresql+asyncpg://[user]:[password]@[host]:[port]/[database]`

## Caching & Rate Limiting

- **REDIS_BROKER_URL**
  - What to put: `redis://host:port/database_number`
  - Purpose: Redis connection URL for rate limiting and caching functionality
  - How to get:
    - **Local Development**: `redis://localhost:6379/0`
    - **Docker Compose**: `redis://redis:6379/0` (when using docker-compose)
    - **Production**: Get from your Redis provider (Redis Cloud, AWS ElastiCache, etc.)
    - **Format**: `redis://[password@]host:port[/database]`

## Security

- **SECRET_KEY**
  - What to put: A secure random string (minimum 32 characters)
  - Purpose: JWT token signing key for authentication
  - How to get:
    - **Generate with OpenSSL**: `openssl rand -hex 32`
    - **Generate with Python**: `python -c "import secrets; print(secrets.token_hex(32))"`
    - **Generate with Node.js**: `node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"`
    - **Online Generator**: Use a secure random string generator (32+ characters)
    - **Keep it secret**: Never commit this to version control

## Monitoring & Logging

- **LOGFIRE_TOKEN**
  - What to put: Your Pydantic Logfire write token (optional)
  - Purpose: Enables automatic logging and monitoring with Pydantic Logfire
  - How to get:
    1. Go to [Pydantic Logfire](https://logfire.pydantic.dev/)
    2. Sign up or log in to your account
    3. Create a new project
    4. Go to Settings → API Keys
    5. Create a new "Write Token"
    6. Copy the token value
  - **Note**: This is optional - the app works without it, but you'll miss out on structured logging

## Platform-Specific Instructions

### Railway Deployment
1. Go to your Railway project dashboard
2. Click on your service
3. Go to Variables tab
4. Add each environment variable with the appropriate values
5. For `POSTGRES_DATABASE_URL`, Railway provides this automatically when you add a PostgreSQL service
6. For `REDIS_BROKER_URL`, add a Redis service and use the provided URL

### Docker Compose
The `docker-compose.yml` file already includes default values for local development:
```yaml
environment:
  - DEBUG=true
  - LOGFIRE_TOKEN=supersecret
  - POSTGRES_DATABASE_URL=postgresql+asyncpg://behemoth:backend@behemoth_db:5432/behemoth_db
```

### Local Development
1. Copy `.env_sample` to `.env`
2. Fill in the values according to your local setup
3. Make sure PostgreSQL and Redis are running locally

## Tips

- **Do not commit real secrets**. Use environment variables in CI/CD platforms or secret managers.
- **For local dev**, keep `.env` in your repo root (not committed to git).
- **Use strong passwords** for database and Redis connections in production.
- **Rotate secrets regularly** especially in production environments.
- **Use different values** for development, staging, and production environments.
- **Test your environment variables** by running the application and checking the health endpoint.

## Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Check if PostgreSQL is running
   - Verify the connection string format
   - Ensure the database exists

2. **Redis Connection Failed**
   - Check if Redis is running
   - Verify the Redis URL format
   - Test connection with `redis-cli ping`

3. **JWT Authentication Not Working**
   - Ensure `SECRET_KEY` is set and is a secure random string
   - Check that the secret key is the same across all application instances

4. **Logfire Not Working**
   - Verify the `LOGFIRE_TOKEN` is correct
   - Check your Logfire project settings
   - Ensure you have internet connectivity

### Validation Commands

Test your environment setup:
```bash
# Test database connection
uv run python -c "from app.core.database import engine; print('Database OK')"

# Test Redis connection
uv run python -c "import redis; r = redis.from_url('$REDIS_BROKER_URL'); print('Redis OK' if r.ping() else 'Redis Failed')"

# Test JWT secret (if implemented)
uv run python -c "from app.common.auth import TokenGenerator; print('JWT OK')"
```
