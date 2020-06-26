from os import path
from urllib.parse import urlparse, urljoin
import string
import random

from flask import current_app


def randomKey(length=6):
    numbers = string.digits
    return "".join(random.choice(numbers) for x in range(length))


def randomString(length=16):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for x in range(length))


def isSafeUrl(target, request):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ("http", "https") and ref_url.netloc == test_url.netloc


def allowedFile(filename):
    return (
        "." in filename
        and getFileExtension(filename) in current_app.config["UPLOAD_EXTENSIONS"]
    )


def getFileExtension(filename):
    return filename.rsplit(".", 1)[1].lower()
