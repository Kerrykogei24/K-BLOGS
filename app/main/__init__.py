from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options


def create_app(config_name):
    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app


