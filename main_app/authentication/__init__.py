from flask import Blueprint

authentication_bp = Blueprint('athentication_bp', __name__, template_folder="templates")

from main_app.authentication import routes, models