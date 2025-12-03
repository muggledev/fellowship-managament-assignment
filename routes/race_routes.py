from flask import Blueprint, request, jsonify
from controllers.race_controller import *

race_bp = Blueprint("race_bp", __name__)

# CREATE
@race_bp.route("/race", methods=["POST"])
def create_race_route():
    return create_race()

# READ ALL
@race_bp.route("/races", methods=["GET"])
def get_all_races_route():
    return get_races()

# READ ONE
@race_bp.route("/race/<uuid:race_id>", methods=["GET"])
def get_race_by_id_route(race_id):
    return get_race(race_id)

# UPDATE
@race_bp.route("/race/<uuid:race_id>", methods=["PUT"])
def update_race_route(race_id):
    return update_race(race_id)

# DELETE
@race_bp.route("/race/delete/<uuid:race_id>", methods=["DELETE"])
def delete_race_route(race_id):
    return delete_race(race_id)
