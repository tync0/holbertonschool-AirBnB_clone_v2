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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
