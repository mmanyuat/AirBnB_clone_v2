#!/usr/bin/python3

"""using flask modules"""

from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)

def hello_hbnb():
	"""function to return hello"""
	return "Hello HBNB!"

if __name__=="__main__":
	"""Ensure the script directly"""
	app.run(host="0.0.0.0", port=5000)
