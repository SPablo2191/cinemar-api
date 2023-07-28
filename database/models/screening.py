from ..db import db
from .room import Room
import datetime

class Screening(db.Document):
    room = db.EmbeddedDocumentField(Room)
    movie_id = db.StringField(required=True)
    movie_name = db.StringField(required=True)
    available_seats = db.IntegerField()
    screening_date = db.DateTimeField()
    status = db.BooleanField(default=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
