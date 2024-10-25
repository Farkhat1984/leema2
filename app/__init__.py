# app/__init__.py
from flask import Flask
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.controllers.main import main_bp
    app.register_blueprint(main_bp)

    return app