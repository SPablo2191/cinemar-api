from ..db import db
import datetime


class User(db.EmbeddedDocument):
    name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    user_name = db.StringField(required=True, unique=True)
    DNI = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    phone_number = db.StringField(required=True, unique=True)
    birth_date = db.DateTimeField()
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    status = db.BooleanField(default=True)