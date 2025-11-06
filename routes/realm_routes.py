from flask import Blueprint, request, jsonify
from controllers.realm_controller import *

realm_bp = Blueprint("realm_bp", __name__)

# CREATE
@realm_bp.route("/", methods=["POST"])
def create_realm_route():
    return create_realm()

# READ ALL
@realm_bp.route("/", methods=["GET"])
def get_all_realms_route():
    return get_realms()

# READ ONE
@realm_bp.route("/<uuid:realm_id>", methods=["GET"])
def get_realm_by_id_route(realm_id):
    return get_realm(realm_id)

# UPDATE
@realm_bp.route("/<uuid:realm_id>", methods=["PUT"])
def update_realm_route(realm_id):
    return update_realm(realm_id)

# DELETE
@realm_bp.route("/<uuid:realm_id>", methods=["DELETE"])
def delete_realm_route(realm_id):
    return delete_realm(realm_id)
