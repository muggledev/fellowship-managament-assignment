import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

class Abilities(db.Model):
    __tablename__ = "Abilities"

    ability_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ability_name = db.Column(db.String(), nullable=False, unique=True)
    power = db.Column(db.Integer(), default=10)
    hero_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Heroes.hero_id"), nullable=False)

    def __init__(self, ability_name, power, hero_id):
        self.ability_name = ability_name
        self.power = power
        self.hero_id = hero_id

    def new_abilities_obj():
        return Abilities('', 0, '')


class AbilitiesSchema(ma.Schema):
    ability_id = ma.fields.UUID(dump_only=True)
    ability_name = ma.fields.Str(required=True)
    power = ma.fields.Int()
    hero_id = ma.fields.UUID()


ability_schema = AbilitiesSchema()
abilities_schema = AbilitiesSchema(many=True)