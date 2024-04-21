#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""
from flask import Flask

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
    return "Number: {}".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
