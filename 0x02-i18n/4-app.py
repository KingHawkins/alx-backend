#!/usr/bin/env python3
"""
Basic flask app.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__, template_folder="templates")


class Config(object):
    """
    Configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determines best match for supported languages.
    """
    if request.args.get('locale'):
        lang = request.args.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index():
    """
    Implementation.
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    """
    Running.
    """
    app.run(debug=1, host="0.0.0.0", port=5000)
