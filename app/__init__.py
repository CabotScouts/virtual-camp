import os

from flask import Flask
from flask_talisman import Talisman
from flask_compress import Compress
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app.config import loadConfig, setupLogging

talisman = Talisman()
compress = Compress()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
limiter = Limiter(key_func=get_remote_address)


def create_app(config):
    print(" --- Way Out West! --- \n")
    print(f"Launching with { config } config\n")
    setupLogging()

    app = Flask(__name__)
    loadConfig(config, app)

    talisman.init_app(app, content_security_policy=app.config["CSP"])
    compress.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)

    from app.controllers import registerControllers
    from app.models import User, Group, Role
    from app.seed import seed

    seed(app)
    registerControllers(app)
    return app
