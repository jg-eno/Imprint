# Imprint

A modern, LLM-enhanced, flashcard app with spaced repetition.

### Development Notes

To setup:

1. Clone the repo

```bash
git clone https://github.com/vibhaas/imprint.git
```

2. Install everything in `requirements.txt`

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

3. Set-up the MySQL database. The raw SQL is in `docs/db/imprint.sql`.

Create a file named `.env` which should contain:

```
DB_USER='<your_mysql_username>'
DB_PASSWORD='<your_mysql_password>'
DB_HOST='localhost'
DB_NAME='imprint'
GOOGLE_API_KEY='<your_gemini_api_key>'
JWT_SECRET_KEY='<server_jwt_secret_key>'
JWT_ACCESS_TOKEN_EXPIRES_HOURS='48'
```

Generate a unique JWT secret key using Python `secrets` module:

```python
import secrets
print(secrets.token_hex(32))
```

`"JWT_ACCESS_TOKEN_EXPIRES_HOURS"` is set to 48 because the JWT implementation does not have a refresh method or refresh token implemented. This is a future to-do.

4. Run the app

```bash
cd server
python3 app.py
```

**Note:** Currently, the app runs from `localhost:5000`.
