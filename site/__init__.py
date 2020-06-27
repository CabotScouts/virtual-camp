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
login_manager.session_protection = "strong"

## TEST DB DATA
from CabotAtHome.site.models import User, Group
from CabotAtHome.site.models.User import Role

db.create_all()

u = User(username="root", key="1001", role=Role.ADMIN)
db.session.add(u)

groups = [
    "1st Bishopston",
    "3rd Bristol",
    "4th Bristol (1st Southmead)",
    "7th Bristol (Christ Church Clifton)",
    "18th Bristol (1st Redland Green)",
    "26th Bristol (North Cote)",
    "43rd Bristol (St. Mary's Stoke Bishop)",
    "44th Bristol (White Tree)",
    "62nd Bristol (Horfield Methodist and Parish Church)",
    "63rd Bristol (St. Andrew's with St. Bartholomew's)",
    "77th Bristol (Redland Park)",
    "90th Bristol (Westbury Methodists)",
    "91st Bristol (Horfield Baptist)",
    "126th Bristol (Sea Mills)",
    "167th Bristol (Westbury Baptist)",
    "169th Bristol (Brentry)",
    "191st Bristol (St. Mary's Shirehampton)",
    "227th Bristol (St. Peter's)",
    "Bristol Royal Hospital for Children",
    "Cabot Explorers",
    "Gromit Network",
]
for group in groups:
    g = Group(name=group)
    db.session.add(g)

db.session.commit()
## TEST DB DATA

registerControllers(app)
