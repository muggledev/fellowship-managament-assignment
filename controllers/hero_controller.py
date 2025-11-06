from flask import jsonify, request
from db import db
from models.hero import Heroes, hero_schema, heroes_schema
from models.race import Races
from util.reflection import populate_object

# CREATE
def create_hero():
    data = request.get_json()
    if not data or "hero_name" not in data or "race_id" not in data:
        return jsonify({"error": "missing required fields: hero_name and race_id"}), 400

    race = Races.query.filter_by(race_id=data["race_id"]).first()
    if not race:
        return jsonify({"error": "race not found"}), 404

    hero = Heroes(
        hero_name=data["hero_name"],
        age=data.get("age"),
        health_points=data.get("health_points", 100),
        is_alive=data.get("is_alive", True),
        race_id=data["race_id"]
    )
    db.session.add(hero)
    db.session.commit()

    result = hero_schema.dump(hero)
    result["race"] = {"race_id": race.race_id, "race_name": race.race_name}
    return jsonify({"message": "hero created successfully", "results": result}), 201


# READ ALL
def get_heroes():
    heroes = Heroes.query.all()
    results = []
    for h in heroes:
        item = hero_schema.dump(h)
        item["race"] = {"race_id": h.race.race_id, "race_name": h.race.race_name}
        results.append(item)
    return jsonify({"message": "heroes retrieved successfully", "results": results}), 200


# READ ONE
def get_hero(hero_id):
    hero = Heroes.query.filter_by(hero_id=hero_id).first()
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    result = hero_schema.dump(hero)
    result["race"] = {"race_id": hero.race.race_id, "race_name": hero.race.race_name}
    return jsonify({"message": f"hero {hero_id} retrieved successfully", "results": result}), 200


# READ ALIVE
def get_alive_heroes():
    alive_heroes = Heroes.query.filter_by(is_alive=True).all()
    return jsonify({
        "message": "alive heroes retrieved successfully",
        "results": heroes_schema.dump(alive_heroes)
    }), 200


# UPDATE
def update_hero(hero_id):
    hero = Heroes.query.filter_by(hero_id=hero_id).first()
    if not hero:
        return jsonify({"error": "hero not found"}), 404

    data = request.get_json()
    populate_object(hero, data)
    db.session.commit()

    result = hero_schema.dump(hero)
    result["race"] = {"race_id": hero.race.race_id, "race_name": hero.race.race_name}
    return jsonify({"message": f"hero {hero_id} updated successfully", "results": result}), 200


# DELETE
def delete_hero(hero_id):
    hero = Heroes.query.filter_by(hero_id=hero_id).first()
    if not hero:
        return jsonify({"error": "hero not found"}), 404

    db.session.delete(hero)
    db.session.commit()
    return jsonify({"message": "hero deleted successfully"}), 200
