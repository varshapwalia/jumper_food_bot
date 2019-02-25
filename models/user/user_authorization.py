from flask_mongoengine import MongoEngine
from bson.objectid import ObjectId
from ..base import BaseDocument, DefaultDocument, current_datetime

from .user import User

db = MongoEngine()

class Authorization(BaseDocument):
  """A base document defining certain critical fields
    
    #Essential Params
    :param ReferenceField user: User Model Reference
    :param StringField access_token: Assinged Access Token


    #Extra Param
    :param StringField language: Language Used
    :param StringField onesignal_token: One Signal Notification ID
    :param StringField device_type: Device Type Information
   
    """
  user = db.ReferenceField('User')
  access_token = db.StringField(unique=True, required=True)

  language = db.StringField(default="english")
  onesignal_token = db.StringField(default="")
  device_type = db.StringField(default="")

  # Logged in - created_at
  # Last Active - updated_at

  meta = {
    'indexes': ['access_token', 'user', '-updated_at'],
    'ordering': ['-updated_at']
  }

  def set_active(self):
    self.save()
    
def validate_token(token=""):
  if token != "":
    auth = Authorization.objects(access_token=token).first()
    if auth:
      auth.set_active()
      return auth
  return None

def delete_token(token=""):
  auth = Authorization.objects(access_token=token).first()
  if auth:
    auth.delete()
  return True

def logout_from_other_devices(token=""):
  auth = Authorization.objects(access_token=token).first()
  no_of_devices = 0
  if auth:
    auths = Authorization.objects(access_token__ne=token, user=auth.user).all()
    no_of_devices = len(auths)
    auths.delete()
  return "Logout from %s device(s)" % str(no_of_devices)

def count_logged_in_devices(token=""):
  auth = Authorization.objects(access_token=token).first()
  no_of_devices = 0
  if auth:
    auths = Authorization.objects(access_token__ne=token, user=auth.user).all()
    no_of_devices = len(auths)
  return no_of_devices

def delete_user_auth(user_id = ""):
  user = User.objects(id=ObjectId(user_id)).first()
  count = 0
  if user:
    auths = Authorization.objects(user=user).all()
    count = len(auths)
    auths.delete()
  return "Logout from %s device(s)" % str(count)