#!/bin/bash

BASE_DIR=/home/lech/programing/python/soup_io
DJANGO_SETTINGS_MODULE=soup_io.settings

export DJANGO_SETTINGS_MODULE
export PYTHONPATH=$PYTHONPATH:$BASE_DIR/..

echo "-- Using PYTHONPATH: $PYTHONPATH"
echo "-------------------"

$@
