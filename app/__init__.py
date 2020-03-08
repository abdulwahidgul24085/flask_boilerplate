from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config

mail = Mail()
db = SQLAlchemy()

# Application factory, takes config as a parameter var
def create_app(config_name):
    app = Flask(__name__)
    # config from config.py can be imported in the app
    # with from_object
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app,)
    db.init_app(app)

    # attach routes and custom error pages here

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app