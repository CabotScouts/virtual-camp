from flask import Blueprint, render_template

blueprint = Blueprint("errors", __name__)


@blueprint.app_errorhandler(401)
def notFoundError(error):
    return render_template("error.jinja", error=error), 401


@blueprint.app_errorhandler(404)
def notFoundError(error):
    return render_template("error.jinja", error=error), 404


@blueprint.app_errorhandler(504)
def serverError(error):
    return render_template("error.jinja", error=error), 500
