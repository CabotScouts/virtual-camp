from functools import wraps
from flask import redirect, url_for, abort
from flask_login import current_user

from app.models.User import Permission


def needs_group(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if current_user.hasPermission(Permission.GROUP):
            return f(*args, **kwargs)

        elif current_user.get_id() == None:
            # Not logged in - redirect to form
            return redirect(url_for("group.login"))

        else:
            # Logged in but not a Group User
            return abort(403)

    return inner


def needs_manage(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if current_user.hasPermission(Permission.MANAGE):
            return f(*args, **kwargs)

        elif current_user.get_id() == None:
            # Not logged in - redirect to form
            return redirect(url_for("auth.login"))

        else:
            # Logged in but not a Manager
            return abort(403)

    return inner


def needs_admin(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if current_user.hasPermission(Permission.ADMIN):
            return f(*args, **kwargs)

        elif current_user.get_id() == None:
            # Not logged in - redirect to form
            return redirect(url_for("auth.login"))

        else:
            # Logged in but not an Admin
            return abort(403)

    return inner
