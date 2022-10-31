#!/bin/bash
cd /webapp/
nohup .venv/bin/python3 manage.py runserver > nohup_script.out 2>&1 & echo $! > app.pid

