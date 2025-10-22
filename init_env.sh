#!/bin/bash

# Dependencies: coverage, unittest-xml-reporting
# Make it executable in cmdline: 'chmod +x init_env.sh'

python3 -m venv .venv
source .venv/bin/activate
pip install coverage unittest-xml-reporting