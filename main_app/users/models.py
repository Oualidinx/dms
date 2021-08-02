from main_app import db, login_manager
from flask_login import UserMixin
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask import current_app
from main_app import _l

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False, index=True)
    first_name = db.Column(db.String(255), unique=True, nullable=False)
    last_name = db.Column(db.Stirng(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False)
    picture = db.Column(db.String(255))
    password_hash = db.Column(db.String(512), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    last_access = db.Column(db.Datetime, default=datetime.utcnow())
    phone_number = db.Column(db.String(10), nullable=False, unique=True, index=True)
    token = db.Column(db.String(256), nullable=False, unique=True)
    token_expiration = db.Column(db.DateTime)

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password, 'sha256')

    @staticmethod
    def check_password_hash(password_hash, password_to_check):
        return check_password_hash(password_hash, password_to_check)

    def generate_token(self, expiration=24):
        self.token_expiration = datetime.utcnow() + timedelta(hours=expiration)
        self.token = jwt.encode({
            'email': self.email,
            'exp': self.token_expiration
        }, current_app.config['SECRET_KEY'], algorithm='HS256')
        db.session.add(self)
        db.session.commit()
        return self.token

    def delete_token(self):
        self.token = None
        self.token_expiration = None
        db.session.add(self)
        db.session.commit()
        return '', 204

    @staticmethod
    def check_token(user_id):
        user = User.query.get(user_id)
        if user and user.token_expiration >= datetime.utcnow():
            return user
        raise Exception(_l('Invalid or missing token'))


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id) if User.query.get(user_id) else None
