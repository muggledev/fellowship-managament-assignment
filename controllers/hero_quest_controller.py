from flask import jsonify, request
from db import db
from models.hero_quest import HeroQuest, hero_quest_schema, hero_quests_schema
from models.hero import Heroes
from models.quest import Quests
from datetime import datetime
from util.reflection import populate_object

# CREATE
def create_hero_quest():
    data = request.get_json()
    if not data or "hero_id" not in data or "quest_id" not in data:
        return jsonify({"error": "missing required fields: hero_id and quest_id"}), 400

    hero = Heroes.query.filter_by(hero_id=data["hero_id"]).first()
    quest = Quests.query.filter_by(quest_id=data["quest_id"]).first()

    if not hero or not quest:
        return jsonify({"error": "hero or Quest not found"}), 404

    hq = HeroQuest(
        hero_id=data["hero_id"],
        quest_id=data["quest_id"],
        date_joined=data.get("date_joined", datetime.utcnow())
    )
    db.session.add(hq)
    db.session.commit()

    result = hero_quest_schema.dump(hq)
    result["hero"] = {"hero_id": hero.hero_id, "hero_name": hero.hero_name}
    result["quest"] = {"quest_id": quest.quest_id, "quest_name": quest.quest_name}

    return jsonify({"message": "heroQuest created successfully", "results": result}), 201


# READ ALL
def get_hero_quests():
    hqs = HeroQuest.query.all()
    results = []
    for hq in hqs:
        item = hero_quest_schema.dump(hq)
        item["hero"] = {"hero_id": hq.hero.hero_id, "hero_name": hq.hero.hero_name}
        item["quest"] = {"quest_id": hq.quest.quest_id, "quest_name": hq.quest.quest_name}
        results.append(item)
    return jsonify({"message": "heroQuests retrieved successfully", "results": results}), 200


# READ ONE
def get_hero_quest(hero_id, quest_id):
    hq = HeroQuest.query.filter_by(hero_id=hero_id, quest_id=quest_id).first()
    if not hq:
        return jsonify({"error": "heroQuest not found"}), 404

    result = hero_quest_schema.dump(hq)
    result["hero"] = {"hero_id": hq.hero.hero_id, "hero_name": hq.hero.hero_name}
    result["quest"] = {"quest_id": hq.quest.quest_id, "quest_name": hq.quest.quest_name}
    return jsonify({"message": "heroQuest retrieved successfully", "results": result}), 200


# READ ALL QUESTS FOR A SPECIFIC HERO
def get_hero_quests(hero_id):
    hero = Heroes.query.filter_by(hero_id=hero_id).first()
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    hero_quests = HeroQuest.query.filter_by(hero_id=hero_id).all()
    if not hero_quests:
        return jsonify({
            "message": f"Hero '{hero.hero_name}' has no assigned quests",
            "results": []
        }), 200

    results = []
    for hq in hero_quests:
        quest = Quests.query.filter_by(quest_id=hq.quest_id).first()
        if quest:
            quest_data = {
                "quest_id": str(quest.quest_id),
                "quest_name": quest.quest_name,
                "difficulty": quest.difficulty,
                "reward_gold": quest.reward_gold,
                "is_completed": quest.is_completed,
                "date_joined": hq.date_joined
            }
            results.append(quest_data)

    return jsonify({
        "message": f"Quests for hero '{hero.hero_name}' retrieved successfully",
        "results": results
    }), 200


# DELETE
def delete_hero_quest(hero_id, quest_id):
    hq = HeroQuest.query.filter_by(hero_id=hero_id, quest_id=quest_id).first()
    if not hq:
        return jsonify({"error": "heroQuest not found"}), 404

    db.session.delete(hq)
    db.session.commit()
    return jsonify({"message": "heroQuest deleted successfully"}), 200
