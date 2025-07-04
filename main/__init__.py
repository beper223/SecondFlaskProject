from flask import Flask
from .routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key'  # для flash
    # Регистрация blueprint'ов
    register_blueprints(app)

    return app