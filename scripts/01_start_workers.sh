#!/bin/bash

source ../venv/bin/activate
cd ../code
export SIMULATOR=1
rq worker magnumpi-tasks