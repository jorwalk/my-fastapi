#!/usr/bin/env bash

source ./.my_venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

coverage run -m pytest -s
