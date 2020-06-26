from CabotAtHome.site import db, login_manager


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    key = db.Column(db.Integer)
