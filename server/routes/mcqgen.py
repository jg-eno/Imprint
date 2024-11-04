from flask import Blueprint, request, jsonify
from flask_cors import CORS
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash
from config import get_db, bcrypt, jwt

users_bp = Blueprint("users", __name__)

# Signup Route
@users_bp.route("/signup", methods=["POST"])
def signup():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    uname = data.get("username")
    email = data.get("email")
    pwd = data.get("password")

    hashed_pwd = generate_password_hash(pwd)  # Hash the password
    print(hashed_pwd)
    try:
        cursor.execute("SELECT email FROM Users")
        em = cursor.fetchall()
        if (email,) in em:
            return jsonify({"message": "Account Already Exists"}), 400
        else:
            cursor.execute(
                "INSERT INTO Users (email, password, username) VALUES (%s, %s, %s)",
                (email, hashed_pwd, uname),
            )
            db.commit()
            return jsonify({"message": "Signup Successful"}), 201
    except Error as e:
        print(f"Database Error: {e}")
        return jsonify({"message": "Signup Failed"}), 500
    finally:
        cursor.close()

# Login Route
@users_bp.route("/login", methods=["POST"])
def login():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    email = data.get("email")
    pwd = data.get("password")
    try:
        cursor.execute("SELECT password FROM Users WHERE email = %s", (email,))
        result = cursor.fetchone()

        if result:
            db_pwd = result[0]  # Extract password from the tuple
            if check_password_hash(db_pwd, pwd):
                return jsonify({"message": "Login Successful"}), 200
            else:
                return jsonify({"message": "Invalid Credentials"}), 401
        else:
            return jsonify({"message": "Account not registered"}), 404
    except Error as e:
        print(f"Database Error: {e}")
        return jsonify({"message": "Login Failed"}), 500
    finally:
        cursor.close()


if __name__ == "__main__":
    print(
        "Please run imprint/server/app.py instead. See imprint/README.md for details."
    )
