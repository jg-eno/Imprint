from flask import Blueprint, request, jsonify
from mysql.connector import Error
from config import get_db, jwt
from flask_jwt_extended import jwt_required, get_jwt_identity

cards_bp = Blueprint("cards", __name__)

def update_all_cards():
    pass

@cards_bp.route('/cards/add', methods=['POST'])
@jwt_required()
def add_card():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    deck_id = data.get("deck_id")
    card_front = data.get("cardFront")
    card_back = data.get("cardBack")
    card_type = data.get("cardType")

    if not deck_id or not card_front or not card_back or not card_type:
        return jsonify({"error": "Deck ID, cardFront, cardBack, and cardType are required"}), 400

    try:
        cursor.execute("""
            INSERT INTO Cards (deckId, cardFront, cardBack, cardType, isActive, isNew) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (deck_id, card_front, card_back, card_type, 1, 1))  # isActive=0, isNew=1 by default
        db.commit()
        return jsonify({"msg": "Card added successfully"}), 201
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while adding the card"}), 500
    finally:
        cursor.close()

@cards_bp.route('/cards/delete', methods=['POST'])
@jwt_required()
def delete_card():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    card_id = data.get("card_id")

    if not card_id:
        return jsonify({"error": "Card ID is required"}), 400

    try:
        cursor.execute("DELETE FROM Cards WHERE cardID = %s", (card_id,))
        db.commit()
        
        # Check if a card was deleted
        if cursor.rowcount == 0:
            return jsonify({"error": "Card not found"}), 404

        return jsonify({"msg": "Card deleted successfully"}), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while deleting the card"}), 500
    finally:
        cursor.close()

@cards_bp.route('/cards/edit', methods=['POST'])
@jwt_required()
def edit_card():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    card_id = data.get("card_id")
    card_front = data.get("cardFront")
    card_back = data.get("cardBack")
    card_type = data.get("cardType")

    if not card_id or not card_front or not card_back or not card_type:
        return jsonify({"error": "Card ID, cardFront, cardBack, and cardType are required"}), 400

    try:
        cursor.execute("""
            UPDATE Cards 
            SET cardFront = %s, cardBack = %s, cardType = %s 
            WHERE cardID = %s
        """, (card_front, card_back, card_type, card_id))
        db.commit()
        
        # Check if a card was updated
        if cursor.rowcount == 0:
            return jsonify({"error": "Card not found"}), 404

        return jsonify({"msg": "Card updated successfully"}), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while updating the card"}), 500
    finally:
        cursor.close()

@cards_bp.route('/cards/get-card', methods=['POST'])
@jwt_required()
def get_card():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    card_id = data.get("card_id")

    if not card_id:
        return jsonify({"error": "Card ID is required"}), 400

    try:
        cursor.execute("""
            SELECT cardID, cardFront, cardBack, cardType, isActive, isNew 
            FROM Cards 
            WHERE cardID = %s
        """, (card_id,))
        card = cursor.fetchone()

        if not card:
            return jsonify({"error": "Card not found"}), 404

        card_data = {
            "cardID": card[0],
            "cardFront": card[1],
            "cardBack": card[2],
            "cardType": card[3],
            "isActive": card[4],
            "isNew": card[5]
        }

        return jsonify(card_data), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while fetching the card"}), 500
    finally:
        cursor.close()

@cards_bp.route("/cards/update_card", methods=["POST"])
def update_card():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()
    card_id = data.get("card_id")
    q_value = data.get("q_value")
    if not card_id:
        return jsonify({"error": "Card ID is required"}), 400
    if q_value is None:
        return jsonify({"error": "Q-value is required"}), 400
    try:
        query = "SELECT intervalLength, cardEase, repetitions, deckID FROM Cards WHERE cardID = %s"
        cursor.execute(query, (card_id,))
        card = cursor.fetchone()
        if not card:
            return jsonify({"error": "Card not found"}), 404
        interval_length, card_ease, repetitions, deck_id = card

        active_stat = 1

        # Implementing the SM2 algorithm
        if q_value < 3:  # If the answer is low performance
            repetitions = 0
            interval_length = 0  # Reset interval for low performance
            card_ease = max(1.3, card_ease - 0.2)  # Decrease ease
        else:
            active_stat = 0
            if repetitions == 0:
                interval_length = 1
            elif repetitions == 1:
                interval_length = 3
            else:
                interval_length = round(interval_length * card_ease)
            repetitions += 1
            card_ease = min(2.5, card_ease + 0.1 if q_value > 3 else card_ease - 0.2)

        # Update card in database
        update_query = """
          UPDATE Cards 
          SET intervalLength = %s, cardEase = %s, repetitions = %s, isActive = %s, isNew = %s, previousReviewDate = CURDATE() 
          WHERE cardID = %s
          """
        cursor.execute(update_query, (interval_length, card_ease, repetitions, active_stat, 1, card_id))
        db.commit()

        """
        old user stat code
        user_id_query = "SELECT UserId FROM Decks WHERE DeckId = %s"
        cursor.execute(user_id_query, (deck_id,))
        user_id = cursor.fetchone()[0]

        update_user_stats_query = ".""
          UPDATE UserStats 
          SET learningPace = learningPace + 1, deckCount = deckCount + 1 
          WHERE userId = %s
          ""."
        cursor.execute(update_user_stats_query, (user_id,))
        db.commit()
        """

        return (
            jsonify(
                {
                    "msg": "Card updated successfully!"
                }
            ),
            200,
        )
    except Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()


if __name__ == "__main__":
    print(
        "Please run imprint/server/app.py instead. See imprint/README.md for details."
    )
