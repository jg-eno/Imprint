from flask import Flask, g
from config import get_db_connection
from routes.decks import decks_bp
from routes.cards import cards_bp
from routes.users import users_bp

app = Flask(__name__)

# Database Connection creation for the current request
# (ensures each request has exactly db connection, closes it after the request)
def get_db():
    if 'db' not in g:
        g.db = get_db_connection()
    return g.db

@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop('db', None)
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