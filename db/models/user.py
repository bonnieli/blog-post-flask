from sqlalchemy.orm import validates
from sqlalchemy import event
from ..shared import db

import bcrypt


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column("password", db.String, nullable=False)
    salt = db.Column(db.String, nullable=False)
    posts = db.relationship("Post", secondary="user_posts", viewonly=True)

    createdAt = db.Column(db.DateTime, server_default=db.func.now())
    updatedAt = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    @validates("password")
    def validate_username(self, key, password) -> str:
        if len(password) < 6:
            raise ValueError("Password too short")
        return password

    def correct_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password)


def create_salt():
    return bcrypt.gensalt()


def create_password(password, salt):
    return bcrypt.hashpw(password.encode("utf-8"), salt)


@event.listens_for(User, "before_insert")
def set_salt_and_password(mapper, connect, user):
    user.salt = create_salt()
    user.password = create_password(user.password, user.salt)


@event.listens_for(User, "before_update")
def update_salt_and_password(mapper, connect, user):
    user.salt = create_salt()
    user.password = create_password(user.password, user.salt)
