import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

class Quests(db.Model):
    __tablename__ = "Quests"

    quest_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quest_name = db.Column(db.String(), nullable=False, unique=True)
    difficulty = db.Column(db.String())
    reward_gold = db.Column(db.Integer(), default=0)
    is_completed = db.Column(db.Boolean(), default=False)
    location_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Locations.location_id"), nullable=False)

    heroes = db.relationship("HeroQuest", backref="quest", cascade="all, delete-orphan")


class QuestsSchema(ma.Schema):
    quest_id = ma.fields.UUID(dump_only=True)
    quest_name = ma.fields.Str(required=True)
    difficulty = ma.fields.Str()
    reward_gold = ma.fields.Int()
    is_completed = ma.fields.Bool()
    location_id = ma.fields.UUID()


quest_schema = QuestsSchema()
quests_schema = QuestsSchema(many=True)
