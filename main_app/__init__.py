from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_restplus import Api
from configuration import config
from flask_babel import Babel, _

db = SQLAlchemy()
mail = Mail()
babel = Babel()
login_manager = LoginManager()
dms_api = Api()
application = Flask(__name__)


def create_app(config_name):
    application.config.from_object(config[config_name])
    db.init_app(application)
    babel.init_app(application)
    mail.init_app(application)
    login_manager.init_app(application)
    login_manager.login_message = _('You should first login to use this service')

    from main_app.authentication import authentication_bp as auth_bp
    application.register_blueprint(auth_bp, url_prefix="/auth/")

    return application


