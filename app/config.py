class Config:
    SECRET_KEY = "cats"

    UPLOAD_FOLDER = "app/uploads"
    UPLOAD_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "mov", "mp4", "avi"}

    SQLALCHEMY_TRACK_MODIFICATIONS = False
