from flask import Blueprint, render_template, jsonify
from flask_login import current_user
from sqlalchemy import inspect

from core.models import Properties

profile = Blueprint("profile", __name__)


@profile.route("/account")
def account():
    user_data = current_user
    user_dict = {
        c.key: getattr(user_data, c.key) for c in inspect(user_data).mapper.column_attrs
    }
    print(user_dict)
    properties_data = Properties.query.all()
    properties_dict = [
        {
            c.key: getattr(property_data, c.key)
            for c in inspect(property_data).mapper.column_attrs
        }
        for property_data in properties_data
    ]
    print(properties_dict)
    return render_template(
        "seller_list.html", user_data=user_dict, properties_data=properties_dict
    )
