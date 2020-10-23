#!/bin/bash

NAME="shopkeeper"
DJANGODIR=/home/ubuntu/main/shopkeeper
SOCKFILE=/home/ubuntu/main/env/run/gunicorn.sock
USER=ubuntu
GROUP=ubuntu
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=shopkeeper.settings
DJANGO_WSGI_MODULE=shopkeeper.wsgi

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/ubuntu/main/env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
