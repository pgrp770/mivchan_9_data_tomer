from flask import Blueprint

purchase_bluprint = Blueprint("purchase", __name__)

@purchase_bluprint.route("/", methods=["GET"])
def a():
    return "hello"