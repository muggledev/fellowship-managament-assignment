from flask import jsonify, request
from db import db
from models.race import Races, race_schema, races_schema
from util.reflection import populate_object

# CREATE
def create_race():
    data = request.get_json()

    new_race = Races.new_race_obj()
    populate_object(new_race, data)

    db.session.add(new_race)
    db.session.commit()

    return jsonify({"message": "race created successfully", "results": race_schema.dump(new_race)}), 201


# READ ALL
def get_races():
    races = Races.query.all()
    return jsonify({"message": "races retrieved successfully", "results": races_schema.dump(races)}), 200


# READ ONE
def get_race(race_id):
    race = Races.query.filter_by(race_id=race_id).first()
    if not race:
        return jsonify({"error": "race not found"}), 404

    return jsonify({"message": f"race {race_id} retrieved successfully", "results": race_schema.dump(race)}), 200


# UPDATE
def update_race(race_id):
    race = Races.query.filter_by(race_id=race_id).first()
    if not race:
        return jsonify({"error": "race not found"}), 404

    data = request.get_json()
    populate_object(race, data)
    db.session.commit()

    return jsonify({"message": f"race {race_id} updated successfully", "results": race_schema.dump(race)}), 200


# DELETE
def delete_race(race_id):
    race = Races.query.filter_by(race_id=race_id).first()
    if not race:
        return jsonify({"error": "race not found"}), 404

    db.session.delete(race)
    db.session.commit()
    return jsonify({"message": "race deleted successfully"}), 200
