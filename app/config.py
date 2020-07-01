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
    SECRET_KEY = "cats"

    COMPRESS_MIMETYPES = [
        "text/html",
        "text/css",
        "text/xml",
        "application/json",
        "application/javascript",
    ]
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500

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
