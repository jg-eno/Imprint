from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

conn = mysql.connector.connect(
     host=os.getenv('DB_HOST', 'localhost'),
     user=os.getenv('DB_USER', 'root'),
     password=os.getenv('DB_PASS', 'password'),
     database=os.getenv('DB_NAME', 'Anki')
)
curr = conn.cursor()

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
