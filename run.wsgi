import os

from dotenv import load_dotenv

activate = "/home/wayoutwest/.virtualenvs/wayoutwest/bin/activate_this.py"
with open(activate) as file_:
    exec(file_.read(), dict(__file__=activate))

from app import create_app

load_dotenv()
application = create_app(os.getenv("ENVIRONMENT"))
