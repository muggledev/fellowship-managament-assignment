from flask import Blueprint, request, jsonify
from controllers.hero_controller import *
from controllers.hero_quest_controller import *

hero_bp = Blueprint("hero_bp", __name__)

# CREATE
@hero_bp.route("/", methods=["POST"])
def create_hero_route():
    return create_hero()

# READ ALL
@hero_bp.route("/", methods=["GET"])
def get_all_heroes_route():
    return get_heroes()

# READ ONE
@hero_bp.route("/<uuid:hero_id>", methods=["GET"])
def get_hero_by_id_route(hero_id):
    return get_hero(hero_id)

# READ ALL ALIVE
@hero_bp.route("/alive", methods=["GET"])
def get_alive_heroes_route():
    return get_alive_heroes()

# HERO QUESTS
@hero_bp.route("/<uuid:hero_id>/quests", methods=["GET"])
def get_hero_quests_route(hero_id):
    return get_hero_quests(hero_id)

# UPDATE
@hero_bp.route("/<uuid:hero_id>", methods=["PUT"])
def update_hero_route(hero_id):
    return update_hero(hero_id)

# DELETE
@hero_bp.route("/<uuid:hero_id>", methods=["DELETE"])
def delete_hero_route(hero_id):
    return delete_hero(hero_id)
