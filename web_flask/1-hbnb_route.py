#!/usr/bin/python3
"""Importing module from flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def H_HBNB():
    """displays hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """displays HBNB"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
