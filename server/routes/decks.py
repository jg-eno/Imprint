from flask import Blueprint, request, jsonify
from mysql.connector import Error
from config import get_db, bcrypt, jwt, blacklist
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, get_jwt_identity
import random
import datetime

decks_bp = Blueprint("decks", __name__)

@decks_bp.route('/users/add-deck', methods=['POST'])
@jwt_required()
def add_deck():
    user_id = get_jwt_identity()
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    deck_name = data.get("deck_name")

    if not deck_name:
        return jsonify({"error": "Deck name is required"}), 400

    try:
        cursor.execute("INSERT INTO Decks (UserId, deckName) VALUES (%s, %s)", (user_id, deck_name))
        db.commit()
        return jsonify({"msg": "Deck added successfully"}), 201
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while adding the deck"}), 500
    finally:
        cursor.close()

@decks_bp.route('/users/delete-deck', methods=['DELETE'])
@jwt_required()
def delete_deck():
    user_id = get_jwt_identity()
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    deck_id = data.get("deck_id")

    if not deck_id:
        return jsonify({"error": "Deck ID is required"}), 400

    try:
        cursor.execute("DELETE FROM Decks WHERE DeckId = %s AND UserId = %s", (deck_id, user_id))
        db.commit()
        
        # Check if a deck was deleted (row count will be 1 if successful, 0 if no matching deck)
        if cursor.rowcount == 0:
            return jsonify({"error": "Deck not found or unauthorized"}), 404

        return jsonify({"msg": "Deck deleted successfully"}), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while deleting the deck"}), 500
    finally:
        cursor.close()

@decks_bp.route('/users/rename-deck', methods=['PUT'])
@jwt_required()
def rename_deck():
    user_id = get_jwt_identity()
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    deck_id = data.get("deck_id")
    new_name = data.get("new_name")

    if not deck_id or not new_name:
        return jsonify({"error": "Deck ID and new name are required"}), 400

    try:
        cursor.execute("UPDATE Decks SET deckName = %s WHERE DeckId = %s AND UserId = %s", (new_name, deck_id, user_id))
        db.commit()
        
        # Check if a deck was updated
        if cursor.rowcount == 0:
            return jsonify({"error": "Deck not found or unauthorized"}), 404

        return jsonify({"msg": "Deck renamed successfully"}), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while renaming the deck"}), 500
    finally:
        cursor.close()

"""
@decks_bp.route("/random_active_card", methods=["POST"])
def get_random_active_card():
    db = get_db()
    cursor = db.cursor()
    data = request.get_json()
    deck_id = data.get("deck_id")
    user_id = data.get("user_id")
    if not deck_id:
        return jsonify({"error": "Deck ID is required"}), 400
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    try:
        query = ""."
        SELECT cardID FROM Cards
        WHERE deckID = %s AND (isDue = 1 OR isNew = 1)
        ""."
        cursor.execute(query, (deck_id,))
        active_cards = cursor.fetchall()
        if not active_cards:
            return jsonify({"error": "No active cards found for this deck"}), 404
        random_card = random.choice(active_cards)
        return jsonify({"cardID": random_card[0]}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


@decks_bp.route("/api/decks/update/<int:user_id>", methods=["GET"])
def update_deck(user_id):
    db = get_db()
    cursor = db.cursor()
    query_decks = (
        "SELECT DeckId, newCardsPerDay, lastLogin FROM Decks WHERE UserId = %s"
    )
    cursor.execute(query_decks, (user_id,))
    decks = cursor.fetchall()
    current_date = datetime.now()
    for deck in decks:
        deck_id, new_cards_per_day, last_login = deck
        if last_login is not None:
            days_since_login = (current_date - last_login).days
        else:
            days_since_login = 0
        cards_to_learn = min(
            new_cards_per_day * days_since_login, get_total_new_cards(deck_id)
        )
        cards_to_activate = get_dormant_cards(deck_id)
        if cards_to_learn > 0:
            update_card_status(deck_id, "new", "learning", cards_to_learn)
        if cards_to_activate > 0:
            update_card_status(deck_id, "dormant", "active", cards_to_activate)

    return jsonify({"message": "Decks updated successfully!"}), 200


def get_total_new_cards(deck_id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT COUNT(*) FROM Cards WHERE DeckId = %s AND Status = 'new'"
    cursor.execute(query, (deck_id,))
    return cursor.fetchone()[0]


def get_dormant_cards(deck_id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT COUNT(*) FROM Cards WHERE DeckId = %s AND Status = 'dormant'"
    cursor.execute(query, (deck_id,))
    return cursor.fetchone()[0]


def update_card_status(deck_id, old_status, new_status, amount):
    db = get_db()
    cursor = db.cursor()
   # query = f".""
     UPDATE Cards 
     SET Status = %s 
     WHERE DeckId = %s AND Status = %s 
     LIMIT %s
     ""."
    cursor.execute(query, (new_status, deck_id, old_status, amount))
    db.commit()
"""

if __name__ == "__main__":
    print(
        "Please run imprint/server/app.py instead. See imprint/README.md for details."
    )
