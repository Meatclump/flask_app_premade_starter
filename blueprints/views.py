from flask import Blueprint

views_bp = Blueprint(name="views", import_name=__name__)

@views_bp.route("/", methods=["GET"])
def index():
    return "Test"