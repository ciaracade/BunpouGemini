# Imported Flask class
from google.colab import userdata
import google.generativeai as genai
from flask import Flask
import gemini.app as app


# Created an instance of the flask class
app = Flask(__name__)

# Configure Google Gemini
GOOGLE_API_KEY = userdata.get(GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)

# route() decorator tells Flask what URl to trigger with our function
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
