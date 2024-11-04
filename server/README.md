## Imprint Sever

This contains all the backend for the imprint application. It runs using flask.

The implemented api endpoints are:

#### /users

1. **`/users/login`**: Logs in a user if valid credentials are recieved.
    - **Request format:** `{"email": "<string, max 255 chars>", "password": "<string, max 255 chars>"}`
    - **Response format:**
        - 200, _Success_: `{"access_token": "<string, jwt access token>"}`
        - 400, _Malformed request_: `{"error": "Malformed request"}`
        - 401, _Unauthorized_: `{"error": "Invalid email or password"}`
        - 500, _Internal Server Error_: `{"error": "An error occurred"}`
2. **`/users/signup`**: Registers a new user if the provided email is unique.
    - **Request format:** `{"email": "<string, max 255 chars>", "password": "<string, max 255 chars>", "username": "<string, max 255 chars>"}`
    - **Response format:**
        - 201, _Created_: `{"access_token": "<string, jwt access token>"}`
        - 400, _Malformed request_: `{"error": "Malformed request"}`
        - 409, _Conflict_: `{"error": "User with this email already exists"}`
        - 500, _Internal Server Error_: `{"error": "An error occurred"}`
