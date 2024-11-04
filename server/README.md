## Imprint Sever

This contains all the backend for the imprint application. It runs using flask.

The implemented api endpoints are:

#### users

1. `users/login`: Logs in a user if valid credentials are recieved.
    - **Request format:** `{"email": "<string, max 255 chars>", "password": "<string, max 255 chars>"}`.
    - **Response format:**
        - 200, Success: `{"access_token": "<string, jwt access token>"}`
        - 400, Malformed request: `{"error": "Malformed request"}`
        - 401, Unauthorized: `{"error": "Invalid email or password"}`
        - 500, Internal Server Error: `{"error": "An error occurred"}`