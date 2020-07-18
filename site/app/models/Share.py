from enum import Enum

from flask import url_for

from app import db, login_manager
from app.utils import randomString, timeAgo

images = {"bmp", "gif", "jpg", "jpeg", "png", "webp"}
videos = {"avi", "mov", "mp4", "webm"}


class ShareType(Enum):
    NONE = 0
    IMAGE = 1
    VIDEO = 2


class Share(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    ip = db.Column(db.String(15), nullable=False)

    name = db.Column(db.String(50))
    file = db.Column(db.String(20), nullable=False)
    filetype = db.Column(db.Enum(ShareType), default=ShareType.NONE)
    comment = db.Column(db.Text)
    caption = db.Column(db.Text)

    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable=False)
    group = db.relationship("Group", backref=db.backref("shares", lazy=True))

    approved = db.Column(db.Boolean, default=False)
    flagged = db.Column(db.Boolean, default=False)
    featured = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Share ({self.id}, {self.file})>"

    def __init__(self, ext, **kwargs):
        super(Share, self).__init__(**kwargs)

        self.parseType(ext)
        self.generateName(ext)

    def parseType(self, ext):
        if ext in images:
            self.filetype = ShareType.IMAGE

        elif ext in videos:
            self.filetype = ShareType.VIDEO

        else:
            self.filetype = ShareType.NONE

    def generateName(self, ext):
        generated = randomString(15)
        check = Share.query.filter_by(file=generated).count()
        if check > 0:
            self.generateName()
        else:
            self.file = f"{generated}.{ext}"

    def isImage(self):
        return self.filetype == ShareType.IMAGE

    def isVideo(self):
        return self.filetype == ShareType.VIDEO

    @property
    def type(self):
        map = {
            ShareType.IMAGE: "Image",
            ShareType.VIDEO: "Video",
            ShareType.NONE: "Unknown",
        }
        return map[self.filetype]

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

    def feature(self, caption):
        self.featured = True
        self.approved = True
        self.caption = caption
        db.session.add(self)
        db.session.commit()

    def unfeature(self):
        self.featured = False
        db.session.add(self)
        db.session.commit()

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

        if self.featured:
            return "Featured"

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

        if self.featured:
            return "info"

        if self.approved:
            return "success"

        return ""

    @property
    def posted(self):
        return timeAgo(self.created_at)

    def serialise(self):
        return dict(
            file=url_for("share.get", image=self.file, _external=True),
            caption=self.caption,
            posted=self.created_at.timestamp(),
            type=self.type.lower(),
        )
