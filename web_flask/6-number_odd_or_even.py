#!/usr/bin/python3
""" importiing flask class """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """greets hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """DIsplays the name"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays c and the text value"""
    return "C " + replace.text('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """displays python and text"""
    return "Python " + replace.text('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """return an integer"""
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """returns an html file"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def even_or_odd(n):
    """ render and even or odd number"""
    parity = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
