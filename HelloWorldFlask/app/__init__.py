from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from .main import main as main_blueprint
from .auth import auth as auth_blueprint

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    # app.register_blueprint(auth_blueprint)
    return app
