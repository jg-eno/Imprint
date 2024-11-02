from flask import Flask
from routes.add_deck import add_deck_bp
from routes.delete_deck import delete_deck_bp


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"