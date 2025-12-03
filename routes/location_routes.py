from flask import Blueprint, request, jsonify
from controllers.location_controller import *

location_bp = Blueprint("location_bp", __name__)

# CREATE
@location_bp.route("/location", methods=["POST"])
def create_location_route():
    return create_location()

# READ ALL
@location_bp.route("/locations", methods=["GET"])
def get_all_locations_route():
    return get_locations()

# READ ONE
@location_bp.route("/location/<uuid:location_id>", methods=["GET"])
def get_location_by_id_route(location_id):
    return get_location(location_id)

# UPDATE
@location_bp.route("/location/<uuid:location_id>", methods=["PUT"])
def update_location_route(location_id):
    return update_location(location_id)

# DELETE
@location_bp.route("/location/delete/<uuid:location_id>", methods=["DELETE"])
def delete_location_route(location_id):
    return delete_location(location_id)
