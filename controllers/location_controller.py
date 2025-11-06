from flask import jsonify, request
from db import db
from models.location import Locations, location_schema, locations_schema
from models.realm import Realms
from util.reflection import populate_object

# CREATE
def create_location():
    data = request.get_json()
    if not data or "location_name" not in data or "realm_id" not in data:
        return jsonify({"error": "missing required fields: location_name and realm_id"}), 400

    realm = Realms.query.filter_by(realm_id=data["realm_id"]).first()
    if not realm:
        return jsonify({"error": "realm not found"}), 404

    location = Locations(
        location_name=data["location_name"],
        danger_level=data.get("danger_level"),
        realm_id=data["realm_id"]
    )
    db.session.add(location)
    db.session.commit()

    result = location_schema.dump(location)
    result["realm"] = {"realm_id": realm.realm_id, "realm_name": realm.realm_name}
    return jsonify({"message": "location created successfully", "results": result}), 201


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
