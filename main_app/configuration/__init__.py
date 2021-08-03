from flask import Blueprint

configuration_bp = Blueprint('Configuration Blueprint', __name__,
                             url_prefix="/configuration", template_folder="templates")

from main_app.configuration import (models, routes)
