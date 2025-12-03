import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime
from datetime import datetime, timezone
from db import db
import marshmallow as ma

class HeroQuest(db.Model):
    __tablename__ = "HeroQuest"

    hero_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Heroes.hero_id"), primary_key=True)
    quest_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Quests.quest_id"), primary_key=True)
    date_joined = db.Column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __init__(self, hero_id, quest_id, date_joined):
        self.hero_id = hero_id
        self.quest_id = quest_id
        self.date_joined = date_joined


class HeroQuestSchema(ma.Schema):
    hero_id = ma.fields.UUID()
    quest_id = ma.fields.UUID()
    date_joined = ma.fields.DateTime()


hero_quest_schema = HeroQuestSchema()
hero_quests_schema = HeroQuestSchema(many=True)
