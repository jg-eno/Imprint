from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Niranjan05@",
    database = "Anki"
)

curr = conn.cursor()
@app.route('/signup', methods=["POST"])
def signup():
    data = request.get_json()
    name=data.get("username")
    email = data.get("email")
    pwd = data.get("password")

    try:
        curr = conn.cursor()
        curr.execute("select * from users where email=%s", (email,))
        user = curr.fetchone()
        if user:
            print("User already exists")
            return jsonify({"message": "User already exists"}), 400
  
        curr.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, pwd))
        conn.commit()
        print("Inserted Successfully")
        return jsonify({"message": "Login Successful"}), 200
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"message": "Invalid credentials"}), 400
    finally:
        curr.close()




@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    pwd = data.get("password")

    try:
        curr = conn.cursor()
        curr.execute("select * from users where email=%s and password=%s", (email, pwd))
        user = curr.fetchone()

        if user:
            print("Login Successful")
            return jsonify({"message": "Login Successful"}), 200
        else:
            print("Invalid credentials")
            return jsonify({"message": "Invalid credentials"}), 400
    except mysql.connector.Error as err:
        print(f"Error: {err}") 
        return jsonify({"message": "Invalid credentials"}), 400       
    finally:
        curr.close()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
