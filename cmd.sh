#!/bin/bash
dos2unix
set -e
if [ "$ENV" = 'DEV' ]; then
  echo "Running Development Server"
  exec python3 "/CatAvatarGenerator/server.py"
else
  echo "Running Production Server"
  exec gunicorn -b 0.0.0.0:5000 CatAvatarGenerator.server:app
fi
