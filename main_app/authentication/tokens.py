from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth
from flask import request, current_app
from main_app.users import User
import jwt
basic_auth = HTTPBasicAuth()
tokenAuth = HTTPTokenAuth(scheme='Bearer')


@tokenAuth.verify_token
def token_required(f):
    @wraps(f)
    def decorator():
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return {"message": "a valid token is missing"}
        try:
            data = jwt.decode(token.split(" ")[1], current_app.config['SECRET_KEY'], algorithm='HS256')
            current_user = User.check_token(data['id'])
        except Exception as exception:
            return {"messages": str(exception)}, 404

        return f()

    return decorator

