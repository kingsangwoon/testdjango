#!/bin/bash
cd /webapp/

. .venv/bin/activate
pip3 install Django==2.1.*
nohup python3 manage.py runserver 0.0.0.0:8000 > nohup_script.out 2>&1 & echo $! > app.pid

