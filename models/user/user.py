from flask_mongoengine import MongoEngine
from ..base import BaseDocument, DefaultDocument, current_datetime
from .user_profile import UserProfile

db = MongoEngine()

class User(BaseDocument):
  """A base document defining certain critical fields
    
    #Essential Params
    :param Emailfield email: Email of the User
    :param StringField username: Username
    :param StringField password: Encrypted Password
    :param EmbeddedDocumentField profile: Embbeded Profile Document with User Information


    #Extra Param
    :param BooleanField email_verifiled: Verification Status of Email
    :param BooleanField on_boarding_flag: All Necessary Profile fields filled Status
    :param DateTimeField last_active: Time when User was Last Active
    :param BooleanField profile_disable: User Side account Disable status
    """
  #Essential Params
  email = db.EmailField(unique=True, required=True)
  username = db.StringField(unique=True, required=True)
  password = db.StringField() # Should be required
  profile = db.EmbeddedDocumentField('UserProfile')
  
  #Extra Param
  profile_status = db.StringField(default="ACTIVE") #ACTIVE, BLOCKED
  user_type = db.StringField(default="USER") #ADMIN, USER
  verified_email = db.BooleanField(default=False)
  profile_disable = db.BooleanField(default=False)
  last_active = db.DateTimeField()

  meta = {
    'indexes': ['-created_at'],
    'ordering': ['-created_at']
  }

def username_exists(username=""):
  if username:
    if User.objects(username=username).first():
      return True
  return False

def email_exists(email=""):
  if email:
    if User.objects(email=email).first():
      return True
  return False