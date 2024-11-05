from flask import Flask, g
from flask_cors import CORS
from datetime import timedelta
from config import Config, jwt, bcrypt
from routes.users import users_bp
from routes.decks import decks_bp
from routes.cards import cards_bp
from routes.llm import llm_bp

app = Flask(__name__)

# set the user auth jwt encryption

app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=Config.JWT_ACCESS_TOKEN_EXPIRES_HOURS)
bcrypt.init_app(app)
jwt.init_app(app)

# allow requests from Vite app
CORS(app, resources={r"/*": {"origins": "*"}})

# For the globally defined get_db method in config.py

@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

app.register_blueprint(users_bp)
app.register_blueprint(decks_bp)
app.register_blueprint(cards_bp)
app.register_blueprint(llm_bp)

@app.route("/")
def hello_world():
    return "<h3>Hello, Imprint!</h3> <p> There is nothing here except the API. Use Vite to access the GUI. </p>"

if __name__ == "__main__":
    app.run()
