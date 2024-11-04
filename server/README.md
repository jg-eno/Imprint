## Imprint Sever

This contains all the backend for the imprint application. It runs using flask.

The implemented api endpoints are:

#### users

1. **`users/login`**: Logs in a user if valid credentials are recieved.
    - **Request format:** `{"email": "<string, max 255 chars>", "password": "<string, max 255 chars>"}`.
    - **Response format:**
        - 200, _Success_: `{"access_token": "<string, jwt access token>"}`
        - 400, _Malformed request_: `{"error": "Malformed request"}`
        - 401, _Unauthorized_: `{"error": "Invalid email or password"}`
        - 500, _Internal Server Error_: `{"error": "An error occurred"}`

