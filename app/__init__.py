from flask import Flask

from app.routes.auth import auth_bp
from app.routes.health import health_bp
from app.core.config import Config
from app.extensions import db, migrate, api, jwt
from app import models as models
from app.routes.users import users_bp
from app.core.exceptions import register_error_handlers


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)  # # This line connects Alembic with SQLAlchemy models:
    api.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(health_bp, url_prefix="/api/v1")
    api.register_blueprint(auth_bp)
    api.register_blueprint(users_bp)

    register_error_handlers(app)

    return app
