import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from CabotAtHome.site.controllers import registerControllers

app = Flask(__name__)
app.config.from_object("CabotAtHome.site.config.Config")

db = SQLAlchemy(app)
login_manager = LoginManager()

login_manager.init_app(app)

## TEST DB DATA
from CabotAtHome.site.models import User, Group, Share

db.create_all()

groups = ["1st Bishopston", "7th Bristol"]
for group in groups:
    g = Group(name=group)
    db.session.add(g)

users = [("owen", 1001)]
for user in users:
    u = User(name=user[0], key=user[1])
    db.session.add(u)

db.session.commit()
## TEST DB DATA

registerControllers(app)
