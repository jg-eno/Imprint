from flask import Blueprint, request, jsonify
from mysql.connector import Error
from config import get_db, bcrypt, jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

users_bp = Blueprint("users", __name__)

@users_bp.route("/login", methods=["POST"])
def login():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Malformed request"}), 400

    email = data.get("email")
    password = data.get("password")

    try:
        cursor.execute("SELECT UserId, password FROM Users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user and bcrypt.check_password_hash(user[1], password):
            access_token = create_access_token(identity=user[0]) # Generate JWT token
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred"}), 500
    finally:
        cursor.close()

@users_bp.route("/signup", methods=["POST"])
def signup():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data or 'username' not in data:
        return jsonify({"error": "Malformed request"}), 400

    email = data.get("email")
    password = data.get("password")
    username = data.get("username")
    hashed_pwd = bcrypt.generate_password_hash(password).decode('utf-8')

    try:
        cursor.execute("INSERT INTO Users (email, password, username) VALUES (%s, %s, %s)", (email, hashed_pwd, username))
        db.commit()

        access_token = create_access_token(identity=email)  # Generate JWT token
        return jsonify(access_token=access_token), 201
    except Error as e:
        print(f"Database error: {e}")
        if e.errno == 1062:  # Duplicate entry error code for MySQL
            return jsonify({"error": "User with this email already exists"}), 409
        return jsonify({"error": "An error occurred"}), 500
    finally:
        cursor.close()

if __name__ == "__main__":
    print(
        "Please run imprint/server/app.py instead. See imprint/README.md for details."
    )