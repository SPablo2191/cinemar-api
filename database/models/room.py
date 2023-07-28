import datetime
from ..db import db
from .seat import Seat

class Room(db.EmbeddedDocument):
    name = db.StringField(required=True, unique=True)
    price = db.FloatField(required=True)
    seats_quantity = db.IntegerField()
    seats = db.ListField(db.EmbeddedDocumentField(Seat))
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
