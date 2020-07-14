from app import db
from app.utils import randomString

# Keep track of live stream walls running and their state
class StreamLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        super(StreamLink, self).__init__(**kwargs)

        self.token = randomString(45)
