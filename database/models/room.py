import datetime
from ..db import db


class Room(db.Document):
    name = db.StringField(required=True, unique=True)
    price = db.FloatField(required=True)
    seats_quantity = db.IntegerField()
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
