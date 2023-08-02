#!/usr/bin/env python3
"""
Basic flask app.
"""
from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")


@app.route("/", strict_slashes=False)
def index():
    """
    Implementation.
    """
    return render_template("index.html")


if __name__ == "__main__":
    """
    Running.
    """
    app.run(debug=1, host="0.0.0.0", port=5000)
