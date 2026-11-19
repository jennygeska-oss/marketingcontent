from flask import Flask

from app.extensions import db, migrate


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config["CONFIG_NAME"] = config_name

    if config_name == "testing":
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"

    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register the blueprint while create_app() runs
    from app.blueprints import main_bp
    app.register_blueprint(main_bp)

    return app
