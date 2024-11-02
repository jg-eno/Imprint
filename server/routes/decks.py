from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
import random
import datetime

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

@app.route('/api/decks/<int:deck_id>', methods=['DELETE'])
def delete_deck(deck_id):
     query = "DELETE FROM Decks WHERE DeckId = %s"
     try:
          curr.execute(query, (deck_id,))
          conn.commit()
          if curr.rowcount == 0:
               return jsonify({'error': 'Deck not found'}), 404
          return jsonify({'message': f'Deck with ID {deck_id} deleted successfully!'}), 200
     except mysql.connector.Error as err:
          conn.rollback()
          return jsonify({'error': str(err)}), 500

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


@app.route('/api/decks/update/<int:user_id>', methods=['GET'])
def update_deck(user_id):
     query_decks = "SELECT DeckId, newCardsPerDay, lastLogin FROM Decks WHERE UserId = %s"
     curr.execute(query_decks, (user_id,))
     decks = curr.fetchall()
     current_date = datetime.now()
     for deck in decks:
          deck_id, new_cards_per_day, last_login = deck
          if last_login is not None:
               days_since_login = (current_date - last_login).days
          else:
               days_since_login = 0
          cards_to_learn = min(new_cards_per_day * days_since_login, get_total_new_cards(deck_id))
          cards_to_activate = get_dormant_cards(deck_id)
          if cards_to_learn > 0:
               update_card_status(deck_id, 'new', 'learning', cards_to_learn)
          if cards_to_activate > 0:
               update_card_status(deck_id, 'dormant', 'active', cards_to_activate)

     return jsonify({'message': 'Decks updated successfully!'}), 200

def get_total_new_cards(deck_id):
     query = "SELECT COUNT(*) FROM Cards WHERE DeckId = %s AND Status = 'new'"
     curr.execute(query, (deck_id,))
     return curr.fetchone()[0]

def get_dormant_cards(deck_id):
     query = "SELECT COUNT(*) FROM Cards WHERE DeckId = %s AND Status = 'dormant'"
     curr.execute(query, (deck_id,))
     return curr.fetchone()[0]

def update_card_status(deck_id, old_status, new_status, amount):
     query = f"""
     UPDATE Cards 
     SET Status = %s 
     WHERE DeckId = %s AND Status = %s 
     LIMIT %s
     """
     curr.execute(query, (new_status, deck_id, old_status, amount))
     conn.commit()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

