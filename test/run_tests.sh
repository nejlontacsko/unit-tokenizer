#!/bin/bash

# Dependencies: coverage, unittest-xml-reporting
# Make it executable in cmdline: 'chmod +x run_tests.sh'

source ../.venv/bin/activate
coverage run -m unittest discover -s . -p "test_*.py"
coverage xml