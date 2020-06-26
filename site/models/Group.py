from CabotAtHome.site import db, login_manager
from CabotAtHome.site.utils import randomKey


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    key = db.Column(db.Integer)

    def __repr__(self):
        return f"<Group { self.name }>"

    def __init__(self, **kwargs):
        super(Group, self).__init__(**kwargs)
        self.generateKey()

    def generateKey(self):
        self.key = randomKey(6)
