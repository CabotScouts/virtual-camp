from flask_login import UserMixin

from CabotAtHome.site import db, login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    key = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.id}>"
