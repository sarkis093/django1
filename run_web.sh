#!/bin/sh

apt-get update && apt-get upgrade && apt-get install -y libsqlite3-dev
echo "Update system done.."
pip3 install --upgrade pip
pip install -r requirements.txt
echo "pip3 done..."
python3 manage.py migrate
echo "migrate done..."
sleep 2
echo "script run_web.sh done..."