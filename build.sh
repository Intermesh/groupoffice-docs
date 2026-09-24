#!/bin/bash
BRANCH=$(git rev-parse --abbrev-ref HEAD)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sphinx-build -b html . _build/html/$BRANCH