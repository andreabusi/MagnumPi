#!/bin/bash

cd venv
source bin/activate
export FLASK_APP=magnumpi.py
export SIMULATOR=0
flask run