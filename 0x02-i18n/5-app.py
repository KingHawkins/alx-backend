#!/usr/bin/env python3
"""
Basic flask app.
"""
from flask import Flask, render_template, request, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template("5-index.html")


def get_user():
    """this function returns a user dictionary or None if the ID
    cannot be found or if login_as was not passed"""
    userId = request.args.get('login_as', None)
    if userId:
        return users.get(int(userId))
    return None


@app.before_request
def before_request():
    """this function forces this method to be executed before any other"""
    g.user = get_user()


if __name__ == "__main__":
    """
    Running.
    """
    app.run(debug=1, host="0.0.0.0", port=5000)
