import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object("CabotAtHome.site.config.Config")

db.init_app(app)
login_manager.init_app(app)

links = [
    ("Home", "/"),
    ("Sign Up", "/register"),
    ("Camp Timetable", "/timetable"),
    ("Gallery", "/gallery"),
]

from CabotAtHome.site.controllers import registerControllers

registerControllers(app)
