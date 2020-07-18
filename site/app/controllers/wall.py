from datetime import datetime

from flask import current_app, Blueprint, request, jsonify, url_for
from flask_json import JsonError, json_response

from app.models import Share, Message

blueprint = Blueprint("wall", __name__, url_prefix="/wall")


@blueprint.route("message")
def messages():
    m = Message.query.first()
    response = json_response(message=m.message)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@blueprint.route("shares")
@blueprint.route("shares/<int:number>")
@blueprint.route("shares/<int:number>/<int:page>")
def shares(number=30, page=1):
    all = Share.query.filter_by(approved=True, featured=True)
    shares = all.order_by(Share.id.desc()).paginate(page, number, False)
    serialised = [share.serialise() for share in shares.items]
    response = json_response(
        total=all.count(), count=len(serialised), media=serialised, next=shares.next_num
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
