import os

from dotenv import load_dotenv

from app import create_app

load_dotenv()
application = create_app(os.getenv("ENVIRONMENT"))
