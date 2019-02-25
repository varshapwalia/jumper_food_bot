from flask_mongoengine import MongoEngine
from ..base import BaseDocument, DefaultDocument, current_datetime
from .items import *

db = MongoEngine()

class Merchant(BaseDocument):
  """A base document defining certain critical fields
    
    #Essential Params
    :param StringField merchant_id: Merchant's Clover ID
    :param StringField access_token: Access Token ID

    """
  #Essential Params
  merchant_id = db.StringField(unique=True, required=True)
  access_token = db.StringField(unique=True, required=True)
  

  meta = {
    'indexes': ['-created_at'],
    'ordering': ['-created_at']
  }

def save_merchant(merchant_id,access_token):
  merchant_obj = Merchant.objects(merchant_id=merchant_id).first()
  if not merchant_obj:
    merchant_obj = Merchant(merchant_id=merchant_id,access_token=access_token).save()
    return merchant_obj
  else:
    return merchant_obj


def fetch_merchants():
  merchants = Merchant.objects.all()
  if merchants:
    return merchants
  else:
    return False
