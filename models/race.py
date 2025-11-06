import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

class Races(db.Model):
    __tablename__ = "Races"

    race_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    race_name = db.Column(db.String(), nullable=False, unique=True)
    homeland = db.Column(db.String())
    lifespan = db.Column(db.Integer())

    heroes = db.relationship("Heroes", backref="race", cascade="all, delete-orphan")


class RacesSchema(ma.Schema):
    race_id = ma.fields.UUID(dump_only=True)
    race_name = ma.fields.Str(required=True)
    homeland = ma.fields.Str()
    lifespan = ma.fields.Int()


race_schema = RacesSchema()
races_schema = RacesSchema(many=True)
