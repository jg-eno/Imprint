from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for all routes

# Database Connection Setup
def get_db_connection():
    """Establish and return a new DB connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="Anki"
    )

# Signup Route
@app.route('/signup', methods=["POST"])
def signup():
    data = request.get_json()
    uname = data.get("username")
    email = data.get("email")
    pwd = data.get("password")

    hashed_pwd = generate_password_hash(pwd)  # Hash the password
    print(hashed_pwd)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM Users")
        em = cursor.fetchall()
        if (email,) in em:
            return jsonify({"message": "Account Already Exists"}), 400
        else:
            cursor.execute(
                "INSERT INTO Users (email, password, username) VALUES (%s, %s, %s)",
                (email, hashed_pwd, uname)
            )
            conn.commit()
            return jsonify({"message": "Signup Successful"}), 201
    except Error as e:
        print(f"Database Error: {e}")
        return jsonify({"message": "Signup Failed"}), 500
    finally:
        cursor.close()
        conn.close()

# Login Route
@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    pwd = data.get("password")
    print(email,pwd)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
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
        conn.close()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
