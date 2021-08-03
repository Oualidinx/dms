from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from configuration import config
from flask_babel import Babel, _

from flask_babel import lazy_gettext as _l

db = SQLAlchemy()
mail = Mail()
babel = Babel()
login_manager = LoginManager()
application = Flask(__name__)


def create_app(config_name):
    application.config.from_object(config[config_name])
    config[config_name].init_app(application)
    db.init_app(application)
    babel.init_app(application)
    mail.init_app(application)
    login_manager.init_app(application)
    login_manager.login_message = _('You should first login to use this service')

    '''Authentication'''
    from main_app.authentication import authentication_bp as auth_bp
    application.register_blueprint(auth_bp)

    '''Global configuration'''
    from main_app.configuration import configuration_bp as config_bp
    application.register_blueprint(config_bp)

    '''Users basic operation'''
    from main_app.users import user_bp as user_bp
    application.register_blueprint(user_bp)

    return application


