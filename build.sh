#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python3 manage.py collectstatic --no-input
python3 manage.py migrate
python3 create_superuser.py
python3 populate_content.py
python3 populate_news.py

