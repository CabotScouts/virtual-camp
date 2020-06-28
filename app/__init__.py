import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    # login_manager.session_protection = "strong"

    from app.controllers import registerControllers
    from app.models import User, Group, Role
    from app.seed import seed

    seed(app)
    registerControllers(app)
    return app


app = create_app()
