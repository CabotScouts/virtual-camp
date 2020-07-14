from datetime import datetime

from flask import current_app, Blueprint, request, jsonify, url_for
from flask_json import JsonError, json_response

from app.models import Share, StreamLink

blueprint = Blueprint("wall", __name__, url_prefix="/wall")


# @blueprint.route("init")
# def init():
#     now = datetime.now()
#     then = request.args.get("timestamp")
#     key = request.args.get("key")
#     check = False
#
#     if key and key == current_app.config["STREAM_AUTH_KEY"]:
#         link = StreamLink()
#         return json_response(token=link.token)
#     else:
#         raise JsonError(status=403, error="Incorrect authorisation key")
#
#
# @blueprint.route("heartbeat")
# def heartbeat():
#     pass


@blueprint.route("messages")
def messages():
    pass


@blueprint.route("shares")
@blueprint.route("shares/<int:number>")
@blueprint.route("shares/<int:number>/<int:page>")
def shares(number=30, page=1):
    all = Share.query.filter_by(approved=True, featured=True)
    shares = all.order_by(Share.id.desc()).paginate(page, number, False)
    serialised = [share.serialise() for share in shares.items]
    return json_response(
        total=all.count(), count=len(serialised), media=serialised, next=shares.next_num
    )


@blueprint.route("programme")
def programme():
    return json_response(time="10am", now="Activity A", next="Activity B")
