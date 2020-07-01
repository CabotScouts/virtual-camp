ContentSecurityPolicy = {
    "default-src": [
        "'self'",
        "fonts.googleapis.com",
        "fonts.gstatic.com",
        "*.youtube.com",
    ],
    "img-src": ["*", "data:"],
}


class Config:
    SECRET_KEY = "cats"

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
