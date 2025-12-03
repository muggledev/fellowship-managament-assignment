from flask import jsonify, request
from db import db
from models.location import Locations, location_schema, locations_schema
from models.realm import Realms
from util.reflection import populate_object

# CREATE
def create_location():
    data = request.get_json()

    new_location = Locations.new_location_obj()
    populate_object(new_location, data)

    db.session.add(new_location)
    db.session.commit()

    return jsonify({"message": "location created successfully", "results": location_schema.dump(new_location)}), 201


# READ ALL
def get_locations():
    locations = Locations.query.all()
    results = []
    for loc in locations:
        item = location_schema.dump(loc)
        item["realm"] = {"realm_id": loc.realm.realm_id, "realm_name": loc.realm.realm_name}
        results.append(item)
    return jsonify({"message": "locations retrieved successfully", "results": results}), 200


# READ ONE
def get_location(location_id):
    loc = Locations.query.filter_by(location_id=location_id).first()
    if not loc:
        return jsonify({"error": "location not found"}), 404

    result = location_schema.dump(loc)
    result["realm"] = {"realm_id": loc.realm.realm_id, "realm_name": loc.realm.realm_name}
    return jsonify({"message": f"location {location_id} retrieved successfully", "results": result}), 200


# UPDATE
def update_location(location_id):
    loc = Locations.query.filter_by(location_id=location_id).first()
    if not loc:
        return jsonify({"error": "location not found"}), 404

    data = request.get_json()
    populate_object(loc, data)
    db.session.commit()

    result = location_schema.dump(loc)
    result["realm"] = {"realm_id": loc.realm.realm_id, "realm_name": loc.realm.realm_name}
    return jsonify({"message": f"location {location_id} updated successfully", "results": result}), 200


# DELETE
def delete_location(location_id):
    loc = Locations.query.filter_by(location_id=location_id).first()
    if not loc:
        return jsonify({"error": "location not found"}), 404

    db.session.delete(loc)
    db.session.commit()
    return jsonify({"message": "location deleted successfully"}), 200
