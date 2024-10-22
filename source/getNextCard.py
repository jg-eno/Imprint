from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
import random

app = Flask(__name__)
CORS(app)
conn = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASS', 'password'),
    database=os.getenv('DB_NAME', 'Anki')
)
curr = conn.cursor()

@app.route('/random_active_card', methods=['POST'])
def get_random_active_card():
    data = request.get_json()
    deck_id = data.get('deck_id')
    user_id = data.get('user_id')
    if not deck_id:
        return jsonify({'error': 'Deck ID is required'}), 400
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        query = """
        SELECT cardID FROM Cards
        WHERE deckID = %s AND (isDue = 1 OR isNew = 1)
        """
        curr.execute(query, (deck_id,))
        active_cards = curr.fetchall()
        if not active_cards:
            return jsonify({'error': 'No active cards found for this deck'}), 404
        random_card = random.choice(active_cards)
        return jsonify({'cardID': random_card[0]}), 200
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
