from flask import Blueprint, request, jsonify
from controllers.quest_controller import *

quest_bp = Blueprint("quest_bp", __name__)

# CREATE
@quest_bp.route("/", methods=["POST"])
def create_quest_route():
    return create_quest()

# READ ALL
@quest_bp.route("/", methods=["GET"])
def get_all_quests_route():
    return get_quests()

# READ ONE
@quest_bp.route("/<uuid:quest_id>", methods=["GET"])
def get_quest_by_id_route(quest_id):
    return get_quest(quest_id)

# READ BY DIFFICULTY
@quest_bp.route("/difficulty/<difficulty>", methods=["GET"])
def get_quests_by_difficulty_route(difficulty):
    return get_quests_by_difficulty(difficulty)

# UPDATE
@quest_bp.route("/<uuid:quest_id>", methods=["PUT"])
def update_quest_route(quest_id):
    return update_quest(quest_id)

# MARK COMPLETE
@quest_bp.route("/<uuid:quest_id>/complete", methods=["PUT"])
def mark_quest_complete_route(quest_id):
    return mark_quest_complete(quest_id)

# DELETE
@quest_bp.route("/<uuid:quest_id>", methods=["DELETE"])
def delete_quest_route(quest_id):
    return delete_quest(quest_id)
