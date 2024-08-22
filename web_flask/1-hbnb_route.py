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
