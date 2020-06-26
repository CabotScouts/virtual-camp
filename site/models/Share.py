from CabotAtHome.site import db, login_manager


class Share(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable=False)
    file = db.Column(db.String(120), nullable=False)
    comment = db.Column(db.Text)
    approved = db.Column(db.Boolean, default=False)
    flagged = db.Column(db.Boolean, default=False)
    gallery = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Share {self.id}>"

    def approve(self):
        pass
