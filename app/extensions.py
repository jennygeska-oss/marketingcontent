from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Created without an app. The factory binds them with init_app().
db = SQLAlchemy()
migrate = Migrate()
