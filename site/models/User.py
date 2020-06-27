from enum import Enum
from flask_login import UserMixin

from CabotAtHome.site import db, login_manager
from CabotAtHome.site.utils import randomKey


class UserType(Enum):
    USER = 0x0001
    GROUP = 0x0010
    ADMIN = 0x0100


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    key = db.Column(db.String(6))

    type = db.Column(db.Enum(UserType), nullable=False, default=UserType.USER)

    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    group = db.relationship(
        "Group", backref=db.backref("user", lazy=True, uselist=False),
    )

    def __repr__(self):
        return f"<User ({self.id}, {self.name}, {self.type})>"

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

        if "key" not in kwargs:
            self.generateKey()

    def generateKey(self):
        self.key = randomKey(6)
