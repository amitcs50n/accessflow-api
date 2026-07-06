from flask import Flask

from app.routes.health import health_bp
from app.core.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(health_bp, url_prefix="/api/v1")

    return app
