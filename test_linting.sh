#!/bin/bash
cd /lca-workspace/repos/huggingface__diffusers
echo "Running Ruff check on ip_adapter.py..."
ruff check src/diffusers/loaders/ip_adapter.py
if [ $? -eq 0 ]; then
    echo "Linting passed successfully!"
    exit 0
else
    echo "Linting failed!"
    exit 1
fi