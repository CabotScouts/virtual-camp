import os
from pathlib import Path

from dotenv import load_dotenv

from app.utils import randomString, randomKey

env = Path("..") / ".env"
load_dotenv(dotenv_path=env)

ContentSecurityPolicy = {
    "default-src": [
        "'self'",
        "fonts.googleapis.com",
        "fonts.gstatic.com",
        "docs.google.com",
        "*.youtube.com",
    ],
    "img-src": ["*", "data:"],
}


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


class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevConfig(Config):
    pass


class ProdConfig(Config):
    pass
