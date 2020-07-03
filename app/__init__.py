import os

from flask import Flask
from flask_talisman import Talisman
from flask_compress import Compress
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app.config import ContentSecurityPolicy

talisman = Talisman()
compress = Compress()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
limiter = Limiter(key_func=get_remote_address)


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.LocalConfig")

    talisman.init_app(app, content_security_policy=ContentSecurityPolicy)
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


app = create_app()
