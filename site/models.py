from flask import current_app
from flask_login import UserMixin

from CabotAtHome.site import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    key = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.id}>"


class Share(db.Model):
    __tablename__ = "shares"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable=False)
    file = db.Column(db.String(120), nullable=False)
    comment = db.Column(db.Text)

    def __repr__(self):
        return f"<Share {self.id}>"


class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    key = db.Column(db.Integer)
