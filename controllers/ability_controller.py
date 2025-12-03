from flask import jsonify, request
from models.ability import Abilities, ability_schema, abilities_schema
from models.hero import Heroes
from db import db
from util.reflection import populate_object

# CREATE
def create_ability():
    data = request.get_json()
    new_ability = Abilities.new_abilities_obj()
    populate_object(new_ability, data)

    db.session.add(new_ability)
    db.session.commit()

    return jsonify({
        "message": "ability created successfully",
        "results": ability_schema.dump(new_ability)
    }), 201


# READ ALL
def get_abilities():
    abilities = Abilities.query.all()

    results = []
    for a in abilities:
        item = ability_schema.dump(a)
        item["hero"] = {"hero_id": a.hero.hero_id, "hero_name": a.hero.hero_name}
        results.append(item)

    return jsonify({
        "message": "all abilities retrieved successfully",
        "results": results
    }), 200


# READ ONE
def get_ability(ability_id):
    ability = Abilities.query.filter_by(ability_id=ability_id).first()
    if not ability:
        return jsonify({"error": "ability not found"}), 404

    result = ability_schema.dump(ability)
    result["hero"] = {"hero_id": ability.hero.hero_id, "hero_name": ability.hero.hero_name}

    return jsonify({
        "message": f"ability {ability_id} retrieved successfully",
        "results": result
    }), 200


# UPDATE
def update_ability(ability_id):
    ability = Abilities.query.filter_by(ability_id=ability_id).first()
    if not ability:
        return jsonify({"error": "ability not found"}), 404

    data = request.get_json()

    populate_object(ability, data)

    db.session.commit()

    result = ability_schema.dump(ability)
    result["hero"] = {"hero_id": ability.hero.hero_id, "hero_name": ability.hero.hero_name}

    return jsonify({
        "message": f"ability {ability_id} updated successfully",
        "results": result
    }), 200


# DELETE
def delete_ability(ability_id):
    ability = Abilities.query.filter_by(ability_id=ability_id).first()
    if not ability:
        return jsonify({"error": "ability not found"}), 404

    db.session.delete(ability)
    db.session.commit()
    return jsonify({"message": "ability deleted successfully"}), 200
