from ..db import db
from .user import User



class Reservation(db.Document):
    user = db.EmbeddedDocumentField(User)


    pass
