#!/usr/bin/env bash

source ./.my_venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
pip list --outdated
uvicorn main:app --reload --port 5000 