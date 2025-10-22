#!/bin/bash

# Dependencies: coverage, unittest-xml-reporting
# Make it executable in cmdline: 'chmod +x run_tests.sh'

PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/.. && pwd )"

source ../.venv/bin/activate
coverage run -m unittest discover -s $PROJECT_ROOT -p "test_*.py"
coverage xml