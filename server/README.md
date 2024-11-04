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
        - 201, _Success_: `{{'DeckId': 1, 'deckName': 'Example name'}, ...}`
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