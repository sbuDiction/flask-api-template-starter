from flask import Flask
from flask import request
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)

# enable cors
CORS(app)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn


@app.route("/")
def home_view():
    return {
        "status": 200
    }


# Example endpoint
@app.post('/api/greet')
def greetings():
    message = ""
    username = request.form.get('username')
    timestamp = request.form.get('timestamp')

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO greet (username, created) VALUES (?, ?)', (username, timestamp))
    conn.commit()
    conn.close()

    message = "Hello, " + username

    # response
    return {
        "status": "success",
        "greet_message": message
    }


# returns all the greeted users
@app.get('/api/users')
def get_users():
    conn = get_db_connection()
    users = conn.execute(
        'SELECT * FROM greet ORDER BY id DESC LIMIT 10').fetchall()
    conn.close()

    return {
        "users": users
    }
