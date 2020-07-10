from flask import Blueprint, request, flash, render_template, redirect, url_for

blueprint = Blueprint("root", __name__)


@blueprint.app_context_processor
def injectLinks():
    # Inject main menu links into every template render automatically
    return dict(
        links=[
            ("Home", "The event homepage", url_for("root.index")),
            ("Sign Up", "Sign up for the event", url_for("root.register")),
            # (
            #     "Camp Programme",
            #     "The programme for the weekend",
            #     url_for("root.programme"),
            # ),
            (
                "Gallery",
                "A gallery of images and videos sent into the event",
                url_for("share.gallery"),
            ),
        ]
    )


@blueprint.route("/")
def index():
    return render_template("root/index.jinja")


@blueprint.route("/organisation")
def information():
    return render_template("root/information.jinja")


@blueprint.route("/register")
def register():
    return render_template("root/registration.jinja")


# @blueprint.route("/programme")
# def programme():
#     return render_template("root/programme.jinja")


@blueprint.route("/live")
def live():
    return render_template("root/live.jinja")
