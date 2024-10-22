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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
