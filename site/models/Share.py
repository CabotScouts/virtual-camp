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
    file = db.Column(db.String(20), nullable=False)
    comment = db.Column(db.Text)

    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable=False)
    group = db.relationship("Group", backref=db.backref("shares", lazy=True))

    approved = db.Column(db.Boolean, default=False)
    flagged = db.Column(db.Boolean, default=False)
    starred = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Share ({self.id}, {self.file})>"

    def __init__(self, ext, **kwargs):
        super(Share, self).__init__(**kwargs)
        self.generateName(ext)

    def generateName(self, ext):
        generated = randomString(15)
        check = Share.query.filter_by(file=generated).count()
        if check > 0:
            self.generateName()
        else:
            self.file = f"{generated}.{ext}"

    def approve(self):
        self.approved = True
        self.flagged = False
        db.session.add(self)
        db.session.commit()

    def flag(self):
        self.flagged = True
        self.approved = False
        db.session.add(self)
        db.session.commit()

    def star(self):
        self.starred = not self.starred
        self.approved = True
        db.session.add(self)
        db.session.commit()
        return self.starred

    def delete(self):
        self.deleted = True
        db.session.add(self)
        db.session.commit()

    @property
    def status(self):
        if self.flagged:
            return "Flagged"

        if not self.approved:
            return "Pending"

        if self.starred:
            return "Starred"

        if self.approved:
            return "Approved"

        return ""

    @property
    def statusColour(self):
        # Map status of share to a bootstrap class
        if self.flagged:
            return "danger"

        if not self.approved:
            return "warning"

        if self.starred:
            return "info"

        if self.approved:
            return "success"

        return ""
