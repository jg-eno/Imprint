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


@app.route('/api/decks/<int:deck_id>/stats', methods=['GET'])
def get_deck_stats(deck_id):
     query = "SELECT * FROM Decks WHERE DeckId = %s"
     try:
          curr.execute(query, (deck_id,))
          deck = curr.fetchone()
          if deck is None:
               return jsonify({'error': 'Deck not found'}), 404
          deck_stats = {
               'DeckId': deck[0],
               'UserId': deck[1],
               'deckName': deck[2],
               'noOfCards': deck[3],
               'freqRate': deck[4],
               'heatMapString': deck[5],
               'newCardsPerDay': deck[6]
          }
          return jsonify(deck_stats), 200
     except mysql.connector.Error as err:
          return jsonify({'error': str(err)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
