from flask import Blueprint, redirect, url_for, render_template, request, session

views_bp = Blueprint(name="views", import_name=__name__, template_folder="templates")

@views_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")
