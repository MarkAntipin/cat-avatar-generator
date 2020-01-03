#!/bin/bash
dos2unix
set -e
if [ "$ENV" = 'DEV' ]; then
  echo "Running Development ServerHello"
  exec python3 "server.py"
else
  echo "Running Production Server"
  exec gunicorn -b 0.0.0.0:5000 server:app
fi
