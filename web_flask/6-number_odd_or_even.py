#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Print Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Print HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Print Python <text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Print n if only n is int"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    odd_or_even = "odd" if n % 2 != 0 else "even"
    return render_template("6-number_odd_or_even.html", n=n, odd_or_even=odd_or_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
