# Marketing Content API

A Flask API that helps entrepreneurs and small businesses create, review, and improve captions and hooks for their social media.

## Setup

1. Create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Create your local environment file, then replace the placeholder values (never commit .env):

```
cp .env.example .env
```

4. Check that the app starts:

```
FLASK_APP="app:create_app('development')" flask routes
```

## Environment Variables

The app reads its settings from a `.env` file. `.env.example` lists every variable with a safe placeholder. Copy it to `.env` and fill in your own values. `.env` is listed in `.gitignore` so real secrets never get committed.

| Variable | What it does | Notes |
|---|---|---|
| `SECRET_KEY` | Flask's secret key, used to sign sessions and other secure data | Replace `change-me` with a long random string |
| `DATABASE_URL` | Connection string for the database | Blank in the example; set it to your database location, such as a local SQLite file |
| `APP_NAME` | Display name for the app | Set to `Captions API` by default |
| `JWT_SECRET_KEY` | Key used to sign JSON Web Tokens for authentication | Replace `change-me` with a different long random string than `SECRET_KEY` |

To generate a random key:

```
python3 -c "import secrets; print(secrets.token_hex(32))"
```

## Database Migrations

**Current status:** No database models exist yet, so no migrations have been created or run. The database schema is still empty.

**Planned workflow:** Once the first model (the captions/hooks resource) is added, I'll install Flask-Migrate and handle migrations with these commands:

```
# One time only: set up the migrations folder
flask db init

# After adding or changing a model: generate a migration
flask db migrate -m "describe the change"

# Apply the migration to the database
flask db upgrade
```

Each generated migration file should be reviewed before running `upgrade`, then committed to Git so everyone's database stays in sync.