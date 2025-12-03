import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

class Realms(db.Model):
    __tablename__ = "Realms"

    realm_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    realm_name = db.Column(db.String(), nullable=False, unique=True)
    ruler = db.Column(db.String())

    locations = db.relationship("Locations", backref="realm", cascade="all, delete-orphan")

    def __init__(self, realm_name, ruler):
        self.realm_name = realm_name
        self.ruler = ruler

    def new_realm_obj():
        return Realms('', '')


class RealmsSchema(ma.Schema):
    realm_id = ma.fields.UUID(dump_only=True)
    realm_name = ma.fields.Str(required=True)
    ruler = ma.fields.Str()


realm_schema = RealmsSchema()
realms_schema = RealmsSchema(many=True)
