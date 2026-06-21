# Use a lightweight Python image
FROM python:3.12-slim

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Set working directory
WORKDIR /app

# Copy backend requirements first (better Docker layer caching)
COPY app/backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire repository
COPY . .

# Expose application port
EXPOSE 5000

# Start the Flask application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.backend.app:app"]