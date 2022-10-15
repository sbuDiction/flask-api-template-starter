from flask import Flask
from flask import request
from flask_cors import CORS
from numpy import array
import pickle

app = Flask(__name__)

# enable cors
CORS(app)


@app.route("/")
def home_view():
    return {
        "api_status": "Up and running"
    }


# Example endpoint
@app.post('/api/greet')
def greetings():
    message = ""
    username = request.form.get('username')
    message = "Hello, " + username

    # response
    return {
        "status": "success",
        "greet_message": message
    }
