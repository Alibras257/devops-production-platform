#!/usr/bin/env bash
set -euo pipefail

APP_URL="${APP_URL:-http://localhost}"

echo "Checking health endpoint..."
curl --fail --silent --show-error "$APP_URL/health"

echo
echo "Checking readiness endpoint..."
curl --fail --silent --show-error "$APP_URL/ready"

echo
echo "Deployment verification passed."
