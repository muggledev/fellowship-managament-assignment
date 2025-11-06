from flask import jsonify, request
from db import db
from models.quest import Quests, quest_schema, quests_schema
from models.location import Locations
from models.hero_quest import HeroQuest
from util.reflection import populate_object

# CREATE
def create_quest():
    data = request.get_json()
    if not data or "quest_name" not in data or "location_id" not in data:
        return jsonify({"error": "missing required fields: quest_name and location_id"}), 400

    location = Locations.query.filter_by(location_id=data["location_id"]).first()
    if not location:
        return jsonify({"error": "location not found"}), 404

    quest = Quests(
        quest_name=data["quest_name"],
        difficulty=data.get("difficulty"),
        reward_gold=data.get("reward_gold", 0),
        is_completed=data.get("is_completed", False),
        location_id=data["location_id"]
    )
    db.session.add(quest)
    db.session.commit()

    result = quest_schema.dump(quest)
    result["location"] = {"location_id": location.location_id, "location_name": location.location_name}
    return jsonify({"message": "quest created successfully", "results": result}), 201


# READ ALL
def get_quests():
    quests = Quests.query.all()
    results = []
    for q in quests:
        item = quest_schema.dump(q)
        item["location"] = {"location_id": q.location.location_id, "location_name": q.location.location_name}
        results.append(item)
    return jsonify({"message": "quests retrieved successfully", "results": results}), 200


# READ ONE
def get_quest(quest_id):
    quest = Quests.query.filter_by(quest_id=quest_id).first()
    if not quest:
        return jsonify({"error": "quest not found"}), 404

    result = quest_schema.dump(quest)
    result["location"] = {"location_id": quest.location.location_id, "location_name": quest.location.location_name}
    return jsonify({"message": f"quest {quest_id} retrieved successfully", "results": result}), 200


# READ BY DIFFICULTY
def get_quests_by_difficulty(difficulty):
    quests = Quests.query.filter_by(difficulty=difficulty).all()
    return jsonify({
        "message": f"quests with difficulty '{difficulty}' retrieved successfully",
        "results": quests_schema.dump(quests)
    }), 200


# UPDATE
def update_quest(quest_id):
    quest = Quests.query.filter_by(quest_id=quest_id).first()
    if not quest:
        return jsonify({"error": "quest not found"}), 404

    data = request.get_json()
    populate_object(quest, data)
    db.session.commit()

    result = quest_schema.dump(quest)
    result["location"] = {"location_id": quest.location.location_id, "location_name": quest.location.location_name}
    return jsonify({"message": f"quest {quest_id} updated successfully", "results": result}), 200


# UPDATE
def mark_quest_complete(quest_id):
    quest = Quests.query.filter_by(quest_id=quest_id).first()
    if not quest:
        return jsonify({"error": "quest not found"}), 404

    quest.is_completed = True
    db.session.commit()

    return jsonify({
        "message": f"quest '{quest.quest_name}' marked as completed",
        "results": quest_schema.dump(quest)
    }), 200


# DELETE
def delete_quest(quest_id):
    quest = Quests.query.filter_by(quest_id=quest_id).first()
    if not quest:
        return jsonify({"error": "quest not found"}), 404

    db.session.delete(quest)
    db.session.commit()
    return jsonify({"message": "quest deleted successfully"}), 200
