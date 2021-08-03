from flask import Blueprint

user_bp = Blueprint('user_bp', __name__, template_folder="templates")

from main_app.users import routes, models