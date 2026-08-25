#!/usr/bin/env bash
set -euo pipefail

APP_DIR="${APP_DIR:-$HOME/devops-production-platform}"

echo "Switching to app directory: $APP_DIR"
cd "$APP_DIR"

if [ ! -f .env ]; then
  echo "ERROR: .env file not found in $APP_DIR"
  exit 1
fi

if [ ! -f docker-compose.prod.yml ]; then
  echo "ERROR: docker-compose.prod.yml not found in $APP_DIR"
  exit 1
fi

echo "Pulling latest images..."
docker compose -f docker-compose.prod.yml pull

echo "Starting PostgreSQL first..."
docker compose -f docker-compose.prod.yml up -d postgres

echo "Waiting for PostgreSQL to become healthy..."
until [ "$(docker inspect --format='{{.State.Health.Status}}' postgres-db)" = "healthy" ]; do
  echo "PostgreSQL is not healthy yet. Waiting..."
  sleep 5
done

echo "Running database migrations..."
docker compose -f docker-compose.prod.yml run --rm backend python -m flask --app app.py db upgrade

echo "Starting application services..."
docker compose -f docker-compose.prod.yml up -d

echo "Deployment complete."
docker compose -f docker-compose.prod.yml ps