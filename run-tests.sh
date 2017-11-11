#!/usr/bin/env bash

set -e

py.test flask_shell_bpython.py
cat <<EOF >/tmp/hello.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
EOF
FLASK_APP=/tmp/hello.py flask shell </dev/null
