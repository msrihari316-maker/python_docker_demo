FROM python:3.11-slim

WORKDIR /app

# Update packages, install dependencies if needed, and clean up apt lists cache
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root system group and user
# Disable terminal access for appuser so attackers cannot run shell commands if hacked
RUN groupadd -r appgroup && useradd -r -g appgroup -s /bin/false appuser

# Copy code and transfer ownership to non-root user and group
COPY --chown=appuser:appgroup . .

USER appuser

EXPOSE 8000

# Run using Gunicorn WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
