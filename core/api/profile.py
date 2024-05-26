from flask import Blueprint, render_template, jsonify

profile = Blueprint("profile", __name__)


@profile.route("/account")
def account():
    return render_template("test.html")
