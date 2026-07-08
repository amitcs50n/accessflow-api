from flask import Flask

from app.routes.health import health_bp
from app.core.config import Config
from app.extensions import db, migrate
from app import models as models


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(health_bp, url_prefix="/api/v1")

    return app
