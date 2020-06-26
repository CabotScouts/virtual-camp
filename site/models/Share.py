from CabotAtHome.site import db, login_manager
from CabotAtHome.site.utils import randomString


class Share(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )
    ip = db.Column(db.String(15), nullable=False)

    name = db.Column(db.String(50))
    file = db.Column(db.String(120), nullable=False)
    comment = db.Column(db.Text)

    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable=False)
    group = db.relationship("Group", backref=db.backref("share", lazy=True))

    approved = db.Column(db.Boolean, default=False)
    flagged = db.Column(db.Boolean, default=False)
    gallery = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Share ({self.id}, {self.file})>"

    def __init__(self, ext, **kwargs):
        super(Share, self).__init__(**kwargs)
        self.generateName(ext)

    def generateName(self, ext):
        generated = randomString(12)
        check = Share.query.filter_by(file=generated).count()
        if check > 0:
            self.generateName()
        else:
            self.file = f"{generated}.{ext}"

    def approve(self):
        self.approved = True
