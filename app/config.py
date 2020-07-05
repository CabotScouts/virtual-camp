import os
import logging
from pathlib import Path

from dotenv import load_dotenv

from app.utils import randomString, randomKey, ConsoleFormat

env = Path("..") / ".env"
load_dotenv(dotenv_path=env)


def loadConfig(config, app):
    configs = {
        "development": DevConfig,
        "production": ProdConfig,
    }

    app.config.from_object(configs[config])


class AppFormatter(logging.Formatter):
    colours = {
        logging.DEBUG: ConsoleFormat.Blue,
        logging.INFO: ConsoleFormat.Green,
        logging.WARNING: ConsoleFormat.Yellow,
        logging.ERROR: ConsoleFormat.Red,
    }

    def format(self, record):
        l = f"[%(asctime)s][{ self.colours[record.levelno] }{ ConsoleFormat.Bold }%(levelname)s{ ConsoleFormat.Reset}] %(message)s"
        f = logging.Formatter(l)
        return f.format(record)


def setupLogging():
    level = os.getenv("LOG_LEVEL", "INFO")

    logger = logging.getLogger("app")
    logger.setLevel(level)

    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(AppFormatter())

    logger.addHandler(handler)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", randomString(25))
    ROOT_KEY = os.getenv("ROOT_KEY", randomKey(8))

    COMPRESS_MIMETYPES = [
        "text/html",
        "text/css",
        "text/xml",
        "application/json",
        "application/javascript",
    ]
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500
    SEND_FILE_MAX_AGE_DEFAULT = 31536000

    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
    UPLOAD_FOLDER = "app/uploads"
    UPLOAD_EXTENSIONS = {
        "bmp",
        "gif",
        "jpg",
        "jpeg",
        "png",
        "webp",
        "avi",
        "mov",
        "mp4",
        "webm",
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{ os.getenv('DEV_DB_FILE', '')}"

    CSP = {
        "default-src": [
            "'self'",
            "fonts.googleapis.com",
            "fonts.gstatic.com",
            "docs.google.com",
            "*.youtube.com",
        ],
        "img-src": ["*", "data:"],
    }


class ProdConfig(DevConfig):
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    server = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", "")
    database = os.getenv("DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql://{ user }:{ password }@{ server }:{ port }/{ database }"
    )
