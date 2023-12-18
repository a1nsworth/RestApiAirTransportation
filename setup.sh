#!/bin/bash

echo "...Running Alembic Upgrade..."
alembic upgrade head
echo "current DONE"

cd src

echo "...Starting FastAPI app..."

gunicorn main:app --reload --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000