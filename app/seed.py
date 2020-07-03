from flask import current_app

from app import db
from app.models import User, Group, Role
from app.utils import randomKey


def seed(app):
    with app.app_context():
        print("Creating app database:")

        db.create_all()

        print("Created!\n")
        print("Adding root user:")

        rkey = current_app.config["ROOT_KEY"]
        u = User(username="admin", key=rkey, role=Role.ADMIN)
        db.session.add(u)

        print(f"Root user added, key: { rkey }\n")
        print("Adding Group data:")

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
            print(f"Added { g.name }")

        print("Groups added\n")

        db.session.commit()

        print("Database seeding complete")
