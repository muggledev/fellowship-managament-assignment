import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

class Heroes(db.Model):
    __tablename__ = "Heroes"

    hero_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    hero_name = db.Column(db.String(), nullable=False, unique=True)
    age = db.Column(db.Integer())
    health_points = db.Column(db.Integer(), default=100)
    is_alive = db.Column(db.Boolean(), default=True)
    race_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Races.race_id"), nullable=False)

    abilities = db.relationship("Abilities", backref="hero", cascade="all, delete-orphan")
    quests = db.relationship("HeroQuest", backref="hero", cascade="all, delete-orphan")


class HeroesSchema(ma.Schema):
    hero_id = ma.fields.UUID(dump_only=True)
    hero_name = ma.fields.Str(required=True)
    age = ma.fields.Int()
    health_points = ma.fields.Int()
    is_alive = ma.fields.Bool()
    race_id = ma.fields.UUID()


hero_schema = HeroesSchema()
heroes_schema = HeroesSchema(many=True)
