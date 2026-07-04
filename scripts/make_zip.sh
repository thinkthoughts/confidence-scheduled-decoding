#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
zip -r ../confidence-scheduled-decoding.zip . -x "*.ipynb_checkpoints*" "__pycache__/*"
