activate = "/home/wayoutwest/.virtualenvs/wayoutwest/bin/activate_this.py"
with open(activate) as file_:
    exec(file_.read(), dict(__file__=activate))

from app import create_app

application = create_app("production")
