from flask import Flask

from config import Config as myConfig
from .database.database import db, base


def setup_database(app):
    with app.app_context():
        @app.before_first_request
        def create_tables():
            base.metadata.create_all(db)


def init_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    setup_database(app)

    from .routes import user_bp
    app.register_blueprint(user_bp)

    return app
