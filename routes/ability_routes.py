from flask import Blueprint, request, jsonify
from controllers.ability_controller import *

ability_bp = Blueprint("ability_bp", __name__)

# CREATE
@ability_bp.route("/ability", methods=["POST"])
def create_ability_route():
    return create_ability()

# READ ALL
@ability_bp.route("/ablities", methods=["GET"])
def get_all_abilities_route():
    return get_abilities()

# READ ONE
@ability_bp.route("/ability/<uuid:ability_id>", methods=["GET"])
def get_ability_by_id_route(ability_id):
    return get_ability(ability_id)

# UPDATE
@ability_bp.route("/ability/<uuid:ability_id>", methods=["PUT"])
def update_ability_route(ability_id):
    return update_ability(ability_id)

# DELETE
@ability_bp.route("/ability/delete/<uuid:ability_id>", methods=["DELETE"])
def delete_ability_route(ability_id):
    return delete_ability(ability_id)
