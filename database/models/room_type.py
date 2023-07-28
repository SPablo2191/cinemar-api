from ..db import db
class RoomType(db.Document):
    name = db.StringField(required=True, unique=True)
    value = db.FloatField()