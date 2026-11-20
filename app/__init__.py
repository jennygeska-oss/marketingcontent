from flask import Flask

from app.extensions import db, migrate
from config import config


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register the blueprint while create_app() runs
    from app.blueprints import main_bp
    app.register_blueprint(main_bp)

    return app
