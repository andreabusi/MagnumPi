#!/bin/bash

source ../venv/bin/activate
cd ../code
export SIMULATOR=1
export FLASK_APP=magnumpi.py
flask run