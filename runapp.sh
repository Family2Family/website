#!/bin/sh

if [ -d "./venv" ]
then
  export FLASK_APP=wsgi.py
  export FLASK_ENV=development
  flask run

else
  echo "Error: No python flask virtual environment found"
  echo "(Run Commands: './build_env.sh' then 'source venv/bin/activate' before running './runapp.sh')"

fi