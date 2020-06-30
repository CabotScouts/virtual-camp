from os import path
from urllib.parse import urlparse, urljoin
import string
import random
from datetime import datetime
import math

import inflect

from flask import current_app


def randomKey(length):
    numbers = string.digits
    return "".join(random.choice(numbers) for x in range(length))


def randomString(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for x in range(length))


def pluralise(word, n):
    if abs(n) != 1:
        i = inflect.engine()
        return i.plural(word)
    else:
        return word


def timeAgo(then):
    now = datetime.utcnow()
    diff = now - then

    if diff.seconds < 60:
        seconds = math.floor(diff.seconds)
        return f"{ seconds } { pluralise('second', seconds) } ago"

    elif diff.seconds < 3600:
        minutes = math.floor(diff.seconds / 60)
        return f"{ minutes } { pluralise('minute', minutes) } ago"

    elif diff.seconds < 86400:
        hours = math.floor(diff.seconds / 60 / 60)
        return f"{ hours } { pluralise('hour', hours) } ago"

    else:
        days = math.floor(diff.seconds / 60 / 60 / 24)
        return f"{ days } { pluralise('day', days) } ago"


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
