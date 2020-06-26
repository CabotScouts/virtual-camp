import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from CabotAtHome.site.controllers import registerControllers

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object("CabotAtHome.site.config.Config")

db.init_app(app)
login_manager.init_app(app)

registerControllers(app)
