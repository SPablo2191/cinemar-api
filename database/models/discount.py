import datetime
from ..db import db


class Discount(db.Document):
    name = db.StringField(required=True, unique=True)
    value = db.FloatField()
    day = db.StringField(required=True)
    percentage = db.FloatField()
    description = db.StringField()
    status = db.BooleanField(default=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
