from flask_mongoengine import MongoEngine
from ..base import BaseDocument, DefaultDocument, current_datetime

db = MongoEngine()

class UserProfile(db.EmbeddedDocument):
  """A base document defining certain critical fields
    
    #Essential Params
    :param StringField name: Name of the User
   
    """
  #Essential Params
  full_name = db.StringField(max_length=120)
  image = db.StringField()
  rank = db.IntField(default=0)
  rank_points = db.IntField(default=0)