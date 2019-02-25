from flask_mongoengine import MongoEngine
from ..base import BaseDocument, DefaultDocument, current_datetime
from .merchant import *

db = MongoEngine()

class Items(BaseDocument):
  """A base document defining certain critical fields
    
    #Essential Params
    :param StringField item_id: Unique id sent by clover api
    :param StringField name: name of the item
    :param StringField price: Price of the item
    :param ReferenceField merchant: Reference which merchant it belongs to.
    
    """
  #Essential Params
  item_id = db.StringField(required=True)
  name = db.StringField()
  price = db.IntField()
  merchant = db.ReferenceField('Merchant')
  trained = db.BooleanField(default=False)
  

  meta = {
    'indexes': ['-created_at'],
    'ordering': ['-created_at']
  }

def save_item(element, merchant):
  name = element["name"]
  i_id = element["id"]
  price = element["price"]
  item = Items.objects(item_id=i_id).first()
  if not item:
    Items(merchant=merchant, name=name, item_id=i_id, price=price).save()
  else:
    item.name = name
    item.price = price
    item.save()


def fetch_items(merchant_id):
  merchant = Merchant.objects(merchant_id=merchant_id).first()
  if merchant:
    items = Items.objects(merchant=merchant).all()
    if items:
      return items
    else:
      return False
  else:
    return False

def fetch_intent_items(merchant_id):
  merchant = Merchant.objects(merchant_id=merchant_id).first()
  if merchant:
    items = Items.objects(merchant=merchant, trained=False).all()
    if items:
      return items
    else:
      return False
  else:
    return False
