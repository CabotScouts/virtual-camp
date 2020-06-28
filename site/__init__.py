import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

from CabotAtHome.site.controllers import registerControllers

app = Flask(__name__)
app.config.from_object("CabotAtHome.site.config.Config")

db = SQLAlchemy(app)
login_manager = LoginManager(app)
csrf = CSRFProtect(app)

# login_manager.init_app(app)
# login_manager.session_protection = "strong"

from CabotAtHome.site.seed import seed

seed()

registerControllers(app)
