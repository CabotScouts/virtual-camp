from CabotAtHome.site import db
from CabotAtHome.site.models import User


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f"<Group { self.name }>"

    def __init__(self, **kwargs):
        super(Group, self).__init__(**kwargs)
        self.user = User(name=self.sanitisedName)

    @property
    def sanitisedName(self):
        return self.name.lower().replace(" ", "-")
