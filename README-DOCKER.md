# Docker Setup Guide for Imagylze

This guide explains how to run Imagylze using Docker and Docker Compose.

## Prerequisites

- Docker ([Install Docker](https://docs.docker.com/get-docker/))
- Docker Compose ([Install Docker Compose](https://docs.docker.com/compose/install/))

## Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/Ebuka24Stephen/imagylze.git
cd imagylze
cp .env.example .env
```

### 2. Build and Run

```bash
docker-compose up -d
```

This starts:
- **Redis** on `localhost:6379` (message broker)
- **PostgreSQL** on `localhost:5432` (database)
- **Django** on `http://localhost:8000` (API server)
- **Celery Worker** (background task processor)
- **Celery Beat** (scheduled task runner)

### 3. Initialize Database

```bash
docker-compose exec web python manage.py migrate
```

### 4. Create a Superuser (Optional)

```bash
docker-compose exec web python manage.py createsuperuser
```

### 5. Access the API

- API Root: `http://localhost:8000/api/`
- Admin Panel: `http://localhost:8000/admin/`

## Docker Services

### Web (Django)
- Serves the REST API
- Auto-reloads on code changes (development mode)
- Migrations run automatically on startup

### Celery Worker
- Processes image tasks asynchronously
- Consumes tasks from Redis queue
- Scales by running multiple instances

### Celery Beat
- Schedules periodic tasks
- Manages task scheduling

### Redis
- Message broker for Celery
- Task queue storage
- Result backend

### PostgreSQL
- Primary database (production)
- Auto-starts with credentials from `.env`

## Development Workflow

### Run Bash Commands

```bash
# Django shell
docker-compose exec web python manage.py shell

# Database shell
docker-compose exec db psql -U imagylze -d imagylze

# Redis CLI
docker-compose exec redis redis-cli
```

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f web
docker-compose logs -f celery
```

### Stop Services

```bash
docker-compose down
```

## Production Deployment

1. Update `.env` with production values:
   - Set `DEBUG=False`
   - Generate a strong `SECRET_KEY`
   - Set secure database credentials
   - Configure `ALLOWED_HOSTS`

2. Use `docker-compose.yml` (PostgreSQL will be used)

3. Build and push images to a registry:
   ```bash
   docker build -t your-registry/imagylze:latest .
   docker push your-registry/imagylze:latest
   ```

## Troubleshooting

### Services won't start
```bash
# Check service status
docker-compose ps

# Rebuild images
docker-compose build --no-cache

# Remove volumes and start fresh
docker-compose down -v
docker-compose up -d
```

### Database connection errors
```bash
# Check PostgreSQL logs
docker-compose logs db

# Reset database
docker-compose exec db dropdb imagylze -U imagylze
docker-compose exec web python manage.py migrate
```

### Celery not processing tasks
```bash
# Check Celery logs
docker-compose logs celery

# Restart Celery
docker-compose restart celery
```

### Port already in use
Change ports in `docker-compose.yml`:
```yaml
ports:
  - "8001:8000"  # Use 8001 instead of 8000
```

## Architecture

```
Client → Django (8000) → Redis (6379)
                      ↓
                 Celery Worker
                      ↓
                  Pillow (Image Processing)
                      ↓
                 Media Storage (/media)
```

## Multi-Worker Setup

Scale Celery workers:

```bash
docker-compose up -d --scale celery=3
```

This starts 3 Celery workers for parallel task processing.
