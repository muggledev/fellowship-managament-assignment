from flask import Blueprint
from controllers.hero_quest_controller import (
    create_hero_quest,
    get_hero_quests,
    get_hero_quest,
    delete_hero_quest
)

hero_quest_bp = Blueprint("hero_quest_bp", __name__)

# CREATE
@hero_quest_bp.route("/", methods=["POST"])
def create_hero_quest_route():
    return create_hero_quest()

# READ ALL
@hero_quest_bp.route("/", methods=["GET"])
def get_all_hero_quests_route():
    return get_hero_quests()

# READ ONE
@hero_quest_bp.route("/<uuid:hero_id>/<uuid:quest_id>", methods=["GET"])
def get_hero_quest_route(hero_id, quest_id):
    return get_hero_quest(hero_id, quest_id)

# DELETE
@hero_quest_bp.route("/<uuid:hero_id>/<uuid:quest_id>", methods=["DELETE"])
def delete_hero_quest_route(hero_id, quest_id):
    return delete_hero_quest(hero_id, quest_id)
