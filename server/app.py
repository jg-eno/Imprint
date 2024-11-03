from flask import Flask, g
from flask_cors import CORS
from routes.decks import decks_bp
from routes.cards import cards_bp
from routes.users import users_bp

app = Flask(__name__)

# allow requests from Vite app
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# For the globally defined get_db method in config.py

@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

app.register_blueprint(users_bp)
app.register_blueprint(decks_bp)
app.register_blueprint(cards_bp)

@app.route("/")
def hello_world():
    return "<h3>Hello, Imprint!</h3> <p> There is nothing here except the API. Use Vite to access the GUI </p>"

if __name__ == "__main__":
    app.run()
