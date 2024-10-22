from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)
conn = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASS', 'password'),
    database=os.getenv('DB_NAME', 'Anki')
)
curr = conn.cursor()

@app.route('/decks', methods=['POST'])
def create_deck():
     data = request.get_json()
     deck_name = data.get('deckName')
     if not deck_name:
          return jsonify({'error': 'Deck name is required'}), 400

     user_id = data.get('UserId')
     if user_id is None:
          return jsonify({'error': 'UserId is required'}), 400

     no_of_cards = data.get('noOfCards', 0)
     freq_rate = data.get('freqRate', 0.0)
     heat_map_string = data.get('heatMapString', '')
     new_cards_per_day = data.get('newCardsPerDay', 0)

     query = """
     INSERT INTO Decks (UserId, deckName, noOfCards, freqRate, heatMapString, newCardsPerDay)
     VALUES (%s, %s, %s, %s, %s, %s)
     """
     values = (user_id, deck_name, no_of_cards, freq_rate, heat_map_string, new_cards_per_day)

     try:
          curr.execute(query, values)
          conn.commit()
          deck_id = curr.lastrowid
          return jsonify({'message': 'Deck created successfully!', 'DeckId': deck_id}), 201

     except mysql.connector.Error as err:
          conn.rollback()
          return jsonify({'error': str(err)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

