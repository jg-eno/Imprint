from flask import Blueprint, request, jsonify
from mysql.connector import Error
from config import get_db, jwt
from flask_jwt_extended import jwt_required, get_jwt_identity
import random
import datetime

decks_bp = Blueprint("decks", __name__)

@decks_bp.route('/decks/add-deck', methods=['POST'])
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

@decks_bp.route('/decks/delete-deck', methods=['POST'])
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
        cursor.execute("DELETE FROM Cards WHERE deckID = %s", (deck_id,))
        
        cursor.execute("DELETE FROM Decks WHERE DeckId = %s AND UserId = %s", (deck_id, user_id))
        db.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Deck not found or unauthorized"}), 404

        return jsonify({"msg": "Deck deleted successfully"}), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while deleting the deck"}), 500
    finally:
        cursor.close()


@decks_bp.route('/decks/rename-deck', methods=['POST'])
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

@decks_bp.route('/decks/get-all-cards', methods=['POST'])
@jwt_required()
def get_all_cards():
    user_id = get_jwt_identity()
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    deck_id = data.get("deck_id")

    if not deck_id:
        return jsonify({"error": "Deck ID is required"}), 400

    try:
        cursor.execute("""
            SELECT cardID, cardFront, cardBack, cardType, isActive, isNew 
            FROM Cards 
            WHERE deckId = %s
        """, (deck_id,))
        cards = cursor.fetchall()

        json_data = [
            {
                "cardID": card[0],
                "cardFront": card[1],
                "cardBack": card[2],
                "cardType": card[3],
                "isActive": card[4],
                "isNew": card[5]
            } for card in cards
        ]

        return jsonify(json_data), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while fetching cards"}), 500
    finally:
        cursor.close()

@decks_bp.route('/decks/get-next-card', methods=['POST'])
@jwt_required()
def get_next_card():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    deck_id = data.get("deck_id")

    if not deck_id:
        return jsonify({"error": "Deck ID is required"}), 400

    try:
        query = """
            SELECT cardID, cardFront, cardBack, cardType, isActive, isNew 
            FROM Cards 
            WHERE deckID = %s AND isActive = 1
        """
        cursor.execute(query, (deck_id,))
        active_cards = cursor.fetchall()

        # if there are no active cards
        if not active_cards:
            return jsonify({"error": "No active cards found in this deck"}), 404

        # Select a random card from the active cards
        selected_card = random.choice(active_cards)
        card_data = {
            "cardID": selected_card[0],
            "cardFront": selected_card[1],
            "cardBack": selected_card[2],
            "cardType": selected_card[3],
            "isActive": selected_card[4],
            "isNew": selected_card[5]
        }

        return jsonify(card_data), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while retrieving the card"}), 500
    finally:
        cursor.close()

if __name__ == "__main__":
    print(
        "Please run imprint/server/app.py instead. See imprint/README.md for details."
    )
