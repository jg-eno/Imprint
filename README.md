# imprint

A modern, LLM-enhanced, flashcard app with spaced repetition.

### Development Notes

To setup:

1. Clone the repo

```bash
git clone https://github.com/vibhaas/imprint.git
```

2. Install flask

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install flask
```

3. Set-up the MySQL database. The raw SQL is in `docs/db/imprint.sql`.

Create a file named `.env` which should contain:

```
DB_USER='<your_mysql_username>'
DB_PASSWORD='<your_mysql_password>'
DB_HOST='localhost'
DB_NAME='imprint'
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

and parallely

```bash
cd client
npm run dev
```