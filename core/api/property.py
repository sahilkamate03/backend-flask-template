from flask import Blueprint, jsonify, request, render_template
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import inspect
from core.models import Properties, db
from core.forms import LoginForm, PropertyForm
from datetime import datetime

property = Blueprint("property", __name__)


@property.route("/add_property_details", methods=["POST"])
def add_property_details():
    form = PropertyForm()
    if form.validate_on_submit():
        property_data = Properties(
            seller_id=current_user.get_id(),  # Get the user ID from current_user
            title=form.title.data,
            description=form.description.data,
            place=form.place.data,
            area=form.area.data,
            number_of_bedrooms=form.number_of_bedrooms.data,
            number_of_bathrooms=form.number_of_bathrooms.data,
            nearby_hospitals=form.nearby_hospitals.data,
            nearby_colleges=form.nearby_colleges.data,
            property_type=form.property_type.data,
            furnishing_status=form.furnishing_status.data,
            facing=form.facing.data,
            water_supply=form.water_supply.data,
            gated_security=form.gated_security.data,
            parking=form.parking.data,
            posted_on=datetime.now(),
            age_of_building=form.age_of_building.data,
            balcony=form.balcony.data,
            rent=form.rent.data,
            deposit=form.deposit.data,
        )
        # print(current_user.get_id())
        db.session.add(property_data)
        db.session.commit()
    else:
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                print(f"Error in {fieldName}: {err}")

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
