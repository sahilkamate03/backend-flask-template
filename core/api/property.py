from flask import Blueprint, flash, jsonify, request, render_template
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import inspect
from core.models import Properties, db
from core.forms import LoginForm, PropertyForm
from datetime import datetime
from flask import redirect, url_for
from flask import redirect, url_for

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


@property.route("/property_delete/<int:property_id>")
@login_required
def property_delete(property_id):
    property = Properties.query.filter_by(id=property_id).first()
    db.session.delete(property)
    db.session.commit()
    flash("Property deleted successfully", "success")
    return redirect(url_for("profile.account"))


@property.route("/update_property_form/<int:property_id>")
@login_required
def update_property_form(property_id):
    user_data = current_user
    user_dict = {
        c.key: getattr(user_data, c.key) for c in inspect(user_data).mapper.column_attrs
    }
    form = PropertyForm()
    return render_template(
        "update_property_form.html",
        property_id=property_id,
        user_data=user_dict,
        form=form,
    )


@property.route("/update_property_details/<int:property_id>", methods=["POST"])
@login_required
def update_property_details(property_id):
    form = PropertyForm()
    if form.validate_on_submit():
        property = Properties.query.filter_by(id=property_id).first()
        property.title = form.title.data
        property.description = form.description.data
        property.place = form.place.data
        property.area = form.area.data
        property.number_of_bedrooms = form.number_of_bedrooms.data
        property.number_of_bathrooms = form.number_of_bathrooms.data
        property.nearby_hospitals = form.nearby_hospitals.data
        property.nearby_colleges = form.nearby_colleges.data
        property.property_type = form.property_type.data
        property.furnishing_status = form.furnishing_status.data
        property.facing = form.facing.data
        property.water_supply = form.water_supply.data
        property.gated_security = form.gated_security.data
        property.parking = form.parking.data
        property.age_of_building = form.age_of_building.data
        property.balcony = form.balcony.data
        property.rent = form.rent.data
        property.deposit = form.deposit.data
        db.session.commit()
        return redirect(url_for("home.home_latest"))
    else:
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                print(f"Error in {fieldName}: {err}")

    return jsonify({"message": "Property details updated successfully"})


@property.route("/property/detail/<int:property_id>")
@login_required
def property_detail(property_id):
    user_data = current_user
    user_dict = {
        c.key: getattr(user_data, c.key) for c in inspect(user_data).mapper.column_attrs
    }
    property_data = Properties.query.filter_by(id=property_id).first()
    property_dict = {
        c.key: getattr(property_data, c.key)
        for c in inspect(property_data).mapper.column_attrs
    }
    return render_template(
        "property_detail.html", p_dict=property_dict, user_data=user_dict
    )
