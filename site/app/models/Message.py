from flask_login import current_user

from app import db


class Message(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    updated_by = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")
