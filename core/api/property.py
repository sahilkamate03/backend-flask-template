from flask import Blueprint, jsonify, request
from core.models import Properties, db

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
