#!/bin/bash
cd /webapp/
nohup .venv/bin/python3 manage.py runserver 0.0.0.0:8000 > nohup_script.out 2>&1 & echo $! > app.pid

