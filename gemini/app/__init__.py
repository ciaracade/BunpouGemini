import flask
import gemini.app as app

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (gemini/config.py)
app.config.from_object('gemini.config')
