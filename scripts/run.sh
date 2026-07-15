#!/bin/bash

set -e

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

cd "$PROJECT_ROOT/backend"

source ../.venv/bin/activate

uvicorn app.api.server:app --reload