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

    # from app.seed import seed
    with app.app_context():
        db.create_all()

        u = User(username="root", key=1001, role=Role.ADMIN)
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
            "Cabot Explorers",
            "Gromit Network",
        ]
        for group in groups:
            g = Group(name=group)
            db.session.add(g)

        db.session.commit()

    # seed()
    registerControllers(app)
    return app


app = create_app()
