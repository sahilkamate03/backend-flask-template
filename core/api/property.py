from flask import Blueprint, jsonify, request, render_template
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import inspect
from core.models import Properties, db
from core.forms import LoginForm, PropertyForm

property = Blueprint("property", __name__)


@property.route("/add_details", methods=["POST"])
def add_property_details():
    # Get the input data from the request
    data = request.get_json()

    # Create a new Properties object with the input data
    new_property = Properties(
        seller_id=data["seller_id"],
        title=data["title"],
        description=data["description"],
        place=data["place"],
        area=data["area"],
        number_of_bedrooms=data["number_of_bedrooms"],
        number_of_bathrooms=data["number_of_bathrooms"],
        nearby_hospitals=data["nearby_hospitals"],
        nearby_colleges=data["nearby_colleges"],
        price=data["price"],
        property_type=data["property_type"],
        furnishing_status=data["furnishing_status"],
        facing=data["facing"],
        water_supply=data["water_supply"],
        gated_security=data["gated_security"],
        parking=data["parking"],
        posted_on=data["posted_on"],
        age_of_building=data["age_of_building"],
        balcony=data["balcony"],
        rent=data["rent"],
        deposit=data["deposit"],
    )

    db.session.add(new_property)
    db.session.commit()

    return jsonify({"message": "Property details added successfully"})


@property.route("/property_form")
@login_required
def property_form():
    user_data = current_user
    user_dict = {
        c.key: getattr(user_data, c.key) for c in inspect(user_data).mapper.column_attrs
    }
    print(user_dict)
    form = PropertyForm()
    return render_template("property_form.html", user_data=user_dict, form=form)
