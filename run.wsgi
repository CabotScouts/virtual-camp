import os
import sys

from dotenv import load_dotenv

load_dotenv()

sys.path.append("./app")

from app import create_app

application = create_app(os.getenv("ENVIRONMENT"))
