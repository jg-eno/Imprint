from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable CORS for React
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "Anki"
)
curr = conn.cursor()
@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    pwd = data.get("password")
    curr.execute("INSERT INTO Users (email,password) values (%s,%s)",(email,pwd))
    conn.commit()
    print("Inserted Successfully")
    if email == "test@example.com" and pwd == "password123":
        return jsonify({"message": "Login Successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
