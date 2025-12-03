import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

class Locations(db.Model):
    __tablename__ = "Locations"

    location_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_name = db.Column(db.String(), nullable=False, unique=True)
    danger_level = db.Column(db.Integer())
    realm_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Realms.realm_id"), nullable=False)

    quests = db.relationship("Quests", backref="location", cascade="all, delete-orphan")

    def __init__(self, location_name, danger_level, realm_id):
        self.location_name = location_name
        self.danger_level = danger_level
        self.realm_id = realm_id

    def new_location_obj():
        return Locations('', 0, '')


class LocationsSchema(ma.Schema):
    location_id = ma.fields.UUID(dump_only=True)
    location_name = ma.fields.Str(required=True)
    danger_level = ma.fields.Int()
    realm_id = ma.fields.UUID()


location_schema = LocationsSchema()
locations_schema = LocationsSchema(many=True)
