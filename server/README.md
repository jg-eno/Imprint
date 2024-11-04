## Imprint Sever

This contains all the backend for the imprint application. It runs using flask.

The implemented api endpoints are: (All endpoints only accept **POST** requests)

#### /users

1. **`/users/login`**: Logs in a user if valid credentials are recieved.
    - **Request format:**
      ```json
      {
        "email": "<string, max 255 chars>",
        "password": "<string, max 255 chars>"
      }
      ```
    - **Response format:**
        - 200, _Success_: `{"access_token": "<string, jwt access token>"}`
        - 400, _Malformed request_: `{"error": "Malformed request"}`
        - 401, _Unauthorized_: `{"error": "Invalid email or password"}`
        - 500, _Internal Server Error_: `{"error": "An error occurred"}`
2. **`/users/signup`**: Registers a new user if the provided email is unique.
    - **Request format:**
      ```json
      {
        "username": "<string, max 255 chars>",
        "email": "<string, max 255 chars>",
        "password": "<string, max 255 chars>"
      }
      ```
    - **Response format:**
        - 201, _Success_: `{"access_token": "<string, jwt access token>"}`
        - 400, _Malformed request_: `{"error": "Malformed request"}`
        - 409, _Conflict_: `{"error": "User with this email already exists"}`
        - 500, _Internal Server Error_: `{"error": "An error occurred"}`
3. **`/users/logout`**: Logs out a user. Requires JWT token of current login.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>"
      }
      ```
    - **Response format:**
        - 201, _Success_: `{"msg": "Successfully logged out"}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
4. **`/users/get-user`**: Gets user id and username for current user. Also can be used to test if login worked.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>"
      }
      ```
    - **Response format:**
        - 201, _Success_: `{'user_id': <user_id>, 'username': <username>}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
5. **`/users/get-decks`**: Gets all decks for current user.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>"
      }
      ```
    - **Response format:**
        - 201, _Success_: `[{'DeckId': 1, 'deckName': 'Example name'}, ...]`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.

#### /decks

1. **`/users/add-deck`**: Adds a new deck for the current user.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>",
          "deck_name": "<string, max 255 chars>"
      }
      ```
    - **Response format:**
        - 201, _Success_: `{"msg": "Deck added successfully"}`
        - 400, _Bad Request_: `{"error": "Deck name is required"}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
        - 500, _Internal Server Error_: `{"error": "An error occurred while adding the deck"}`

2. **`/users/delete-deck`**: Deletes a deck for the current user by DeckId.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>",
          "deck_id": "<int>"
      }
      ```
    - **Response format:**
        - 200, _Success_: `{"msg": "Deck deleted successfully"}`
        - 400, _Bad Request_: `{"error": "Deck ID is required"}`
        - 404, _Not Found_: `{"error": "Deck not found or unauthorized"}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
        - 500, _Internal Server Error_: `{"error": "An error occurred while deleting the deck"}`

3. **`/users/rename-deck`**: Renames an existing deck for the current user by DeckId.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>",
          "deck_id": "<int>",
          "new_name": "<string, max 255 chars>"
      }
      ```
    - **Response format:**
        - 200, _Success_: `{"msg": "Deck renamed successfully"}`
        - 400, _Bad Request_: `{"error": "Deck ID and new name are required"}`
        - 404, _Not Found_: `{"error": "Deck not found or unauthorized"}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
        - 500, _Internal Server Error_: `{"error": "An error occurred while renaming the deck"}`
4. **`/users/get-all-cards`**: Return all cards for a given deck specified by DeckId.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>",
          "deck_id": "<int>"
      }
      ```
    - **Response format:**
        - 200, _Success_: 
          ```json
          [
              {
                  "cardID": "<int>",
                  "cardFront": "<string>",
                  "cardBack": "<string>",
                  "cardType": "<string>",
                  "isActive": "<bool>",
                  "isNew": "<bool>"
              },
          ]
          ```
        - 400, _Bad Request_: `{"error": "Deck ID is required"}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
        - 500, _Internal Server Error_: `{"error": "An error occurred while fetching cards"}`
5. **`/decks/get-next-card`**: Retrieves a random active card from a specified deck.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>",
          "deck_id": "<int>"
      }
      ```
    - **Response format:**
        - 200, _Success_: 
          ```json
          {
              "cardID": "<int>",
              "cardFront": "<string>",
              "cardBack": "<string>",
              "cardType": "<string>",
              "isActive": "<bool>",
              "isNew": "<bool>"
          }
          ```
        - 400, _Bad Request_: `{"error": "Deck ID is required"}`
        - 404, _Not Found_: `{"error": "No active cards found in this deck"}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
        - 500, _Internal Server Error_: `{"error": "An error occurred while retrieving the card"}`
    
    - **Functionality**: This endpoint selects a single active card randomly from all active cards within a specified deck. It is to be called when studying cards from a deck.

#### /cards
1. **`/cards/add`**: Adds a new card to a specified deck.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>",
          "deck_id": "<int>",
          "cardFront": "<string, max 255 chars>",
          "cardBack": "<string, max 255 chars>",
          "cardType": "<string, max 50 chars>"
      }
      ```
    - **Response format:**
        - 201, _Success_: `{"msg": "Card added successfully"}`
        - 400, _Bad Request_: `{"error": "Deck ID, cardFront, cardBack, and cardType are required"}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
        - 500, _Internal Server Error_: `{"error": "An error occurred while adding the card"}`

2. **`/cards/delete`**: Deletes a card specified by `cardID`.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>",
          "card_id": "<int>"
      }
      ```
    - **Response format:**
        - 200, _Success_: `{"msg": "Card deleted successfully"}`
        - 400, _Bad Request_: `{"error": "Card ID is required"}`
        - 404, _Not Found_: `{"error": "Card not found"}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
        - 500, _Internal Server Error_: `{"error": "An error occurred while deleting the card"}`

3. **`/cards/edit`**: Edits an existing card’s `cardFront`, `cardBack`, and `cardType` by `cardID`.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>",
          "card_id": "<int>",
          "cardFront": "<string, max 255 chars>",
          "cardBack": "<string, max 255 chars>",
          "cardType": "<string, max 50 chars>"
      }
      ```
    - **Response format:**
        - 200, _Success_: `{"msg": "Card updated successfully"}`
        - 400, _Bad Request_: `{"error": "Card ID, cardFront, cardBack, and cardType are required"}`
        - 404, _Not Found_: `{"error": "Card not found"}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
        - 500, _Internal Server Error_: `{"error": "An error occurred while updating the card"}`

4. **`/cards/get-card`**: Retrieves details for a specified card by `cardID`.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>",
          "card_id": "<int>"
      }
      ```
    - **Response format:**
        - 200, _Success_: 
          ```json
          {
              "cardID": "<int>",
              "cardFront": "<string>",
              "cardBack": "<string>",
              "cardType": "<string>",
              "isActive": "<bool>",
              "isNew": "<bool>"
          }
          ```
        - 400, _Bad Request_: `{"error": "Card ID is required"}`
        - 404, _Not Found_: `{"error": "Card not found"}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
        - 500, _Internal Server Error_: `{"error": "An error occurred while fetching the card"}`

5. **`/cards/update_card`**: Update the review statistics for a card based on user performance, using the SM-2 spaced repetition algorithm.
    - **Request format:** 
      ```json
      {
          "Authorization": "Bearer <users_jwt_token_here>",
          "card_id": "<int>",
          "q_value": "<int, 0-5>"
      }
      ```
    - **Response format:**
        - 200, _Success_: `{"msg": "Card updated successfully!"}`
        - 400, _Bad Request_: `{"error": "Card ID is required"}` or `{"error": "Q-value is required"}`
        - 404, _Not Found_: `{"error": "Card not found"}`
        - 401/422/etc., _JWT Authentication Errors_: JWT key doesn't match.
        - 500, _Internal Server Error_: `{"error": "<error details>"}`
    
    - **SM-2 Algorithm Logic**:
        - **`q_value` < 3**: Reset `repetitions` and `intervalLength`, decrease `cardEase` (minimum 1.3).
        - **`q_value` >= 3**: Mark as inactive (`isActive = 0`), increment `repetitions`, adjust `intervalLength` and `cardEase` based on performance.