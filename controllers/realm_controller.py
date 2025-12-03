from flask import jsonify, request
from db import db
from models.realm import Realms, realm_schema, realms_schema
from util.reflection import populate_object

# CREATE
def create_realm():
    data = request.get_json()

    new_realm = Realms.new_realm_obj()
    populate_object(new_realm)

    db.session.add(new_realm)
    db.session.commit()

    return jsonify({"message": "realm created successfully", "results": realm_schema.dump(new_realm)}), 201


# READ ALL
def get_realms():
    realms = Realms.query.all()
    return jsonify({"message": "realms retrieved successfully", "results": realms_schema.dump(realms)}), 200


# READ ONE
def get_realm(realm_id):
    realm = Realms.query.filter_by(realm_id=realm_id).first()
    if not realm:
        return jsonify({"error": "realm not found"}), 404

    return jsonify({"message": f"realm {realm_id} retrieved successfully", "results": realm_schema.dump(realm)}), 200


# UPDATE
def update_realm(realm_id):
    realm = Realms.query.filter_by(realm_id=realm_id).first()
    if not realm:
        return jsonify({"error": "realm not found"}), 404

    data = request.get_json()
    populate_object(realm, data)
    db.session.commit()

    return jsonify({"message": f"realm {realm_id} updated successfully", "results": realm_schema.dump(realm)}), 200


# DELETE
def delete_realm(realm_id):
    realm = Realms.query.filter_by(realm_id=realm_id).first()
    if not realm:
        return jsonify({"error": "realm not found"}), 404

    db.session.delete(realm)
    db.session.commit()
    return jsonify({"message": "realm deleted successfully"}), 200
