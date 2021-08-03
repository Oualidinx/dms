

from main_app.users import user_bp


@user_bp.route('/')
def index():
    return 'index page'