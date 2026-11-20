# Marketing Content API

A Flask API that helps entrepreneurs and small businesses create, review, and improve captions and hooks for their social media.

## Setup

1. Create and activate a virtual environment:

       python3 -m venv .venv
       source .venv/bin/activate

2. Install dependencies:

       pip install -r requirements.txt

3. Create your local environment file, then replace the placeholder values (never commit .env):

       cp .env.example .env

4. Check that the app starts:

       FLASK_APP="app:create_app('development')" flask routes
