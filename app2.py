from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Python App v2 (GREEN)"
