from flask_login import UserMixin, AnonymousUserMixin

from app import db, login_manager
from app.utils import randomKey


class Permission:
    NONE = 0b00000
    LOGIN = 0b00001
    GROUP = 0b10000
    CURATE = 0b00010
    MANAGE = 0b00100
    ADMIN = 0b01000


class Role:
    GUEST = Permission.NONE
    USER = Permission.LOGIN
    GROUP = Permission.GROUP
    CURATOR = Permission.CURATE | Permission.LOGIN
    MANAGER = Permission.MANAGE | Permission.CURATE | Permission.LOGIN
    ADMIN = Permission.ADMIN | Permission.MANAGE | Permission.CURATE | Permission.LOGIN


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    loginKey = db.Column(db.String(12))

    role = db.Column(db.Integer, nullable=False, default=Role.USER)

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

    @property
    def name(self):
        return self.username or self.group.name

    @property
    def key(self):
        return "*****" if self.id == 1 else self.loginKey

    @key.setter
    def key(self, key):
        self.loginKey = key

    def generateKey(self):
        self.loginKey = randomKey(6)

    def validateKey(self, key):
        return key == self.loginKey

    def hasPermission(self, permission):
        return (self.role & permission) > 0


class Guest(AnonymousUserMixin):
    def hasPermission(self, permission):
        return False


login_manager.anonymous_user = Guest
