from main_app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


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

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password, 'sha256')

    @staticmethod
    def check_password_hash(password_hash, password_to_check):
        return check_password_hash(password_hash, password_to_check)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id) if User.query.get(user_id) else None
