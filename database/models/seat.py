from ..db import db


class Seat(db.EmbeddedDocument):
    name = db.StringField()
    row = db.IntegerField(required=True)
    column = db.IntegerField(required=True)
