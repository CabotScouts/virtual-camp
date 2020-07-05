from app import db
from app.models import User, Role


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __repr__(self):
        return f"<Group { self.name }>"

    def __init__(self, **kwargs):
        super(Group, self).__init__(**kwargs)
        self.user = User(role=Role.GROUP)

    @property
    def sanitisedName(self):
        return self.name.lower().replace(" ", "-")
