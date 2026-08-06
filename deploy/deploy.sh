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

echo "Starting services..."
docker compose -f docker-compose.prod.yml up -d

echo "Deployment complete."
docker compose -f docker-compose.prod.yml ps
