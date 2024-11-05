from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

llm_bp = Blueprint("cards", __name__)

@llm_bp.route('/llm/generate', methods=['POST'])
@jwt_required()
def add_card():
    data = request.get_json()
    question = data.get("question")
    answer = data.get("answer")

    if not question or not answer:
        return jsonify({"error": "Values question and answer is required"}), 400

    pass


if __name__ == "__main__":
    print(
        "Please run imprint/server/app.py instead. See imprint/README.md for details."
    )
