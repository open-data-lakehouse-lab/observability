#!/usr/bin/env bash

set -euo pipefail

echo "Running Ruff check..."
ruff check .

echo "Running MyPy check..."
mypy src

echo "Running Pytest..."
pytest
