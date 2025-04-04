#!/bin/bash
# Simple script to test if the linting issue is fixed

echo "Running Ruff check on ip_adapter.py..."
ruff check src/diffusers/loaders/ip_adapter.py

if [ $? -eq 0 ]; then
    echo "✅ Linting check passed!"
    exit 0
else
    echo "❌ Linting check failed!"
    exit 1
fi