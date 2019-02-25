import urllib2
import requests 
import json
from models.clover import *
import dialogflow

def find_merchant(merchant_id,access_token):
  try:

    mid = merchant_id
    token = access_token

    string = "https://apisandbox.dev.clover.com/v3/merchants/%s/items?access_token=%s" % (mid,token)
    jsoned = json.load(urllib2.urlopen(string))
    if jsoned:
      merchant = save_merchant(mid,token)
      # merchant = True
      if jsoned['elements']:
        for element in jsoned['elements']:
          save_item(element,merchant)
        return "Task complete Items Added/Updated(name/price)"
      else:
        return "No Items Found"
    else:
      return "No Merchant Found"
    
    
  except Exception as e:
    print e
    return "Error Occured while fetching merchant Data"


def create_intent(project_id, display_name, training_phrases_parts,
                  message_texts):
    """Create an intent of the given intent type."""
    import dialogflow_v2 as dialogflow
    intents_client = dialogflow.IntentsClient()

    parent = intents_client.project_agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])

    response = intents_client.create_intent(parent, intent)
    print response

def delete_intent(project_id, intent_id):
    """Delete intent with the given intent type and intent value."""
    import dialogflow_v2 as dialogflow
    intents_client = dialogflow.IntentsClient()

    intent_path = intents_client.intent_path(project_id, intent_id)

    intents_client.delete_intent(intent_path)



def create_dialogues(merchant_id):
  # It will only intialize the bot and will not replace the existing one, 
  # we will need to fetch ids and feed it to delete_intent() for it.
  try:
    project_id = "food-bot-5e773"
    items = fetch_intent_items(merchant_id)
    menu = []
    items_prices = {}
    if items:
      for item in items:
        name = item.name
        price = item.price
        menu.append(name)
        items_prices[name] = price
        item.trained = True
        item.save()
      
      message_texts = ", ".join(menu)
      menu_training = ["what do you have on menu", "which items you have", "menu", "items", "what is there to eat"]
      menu_response = "We have the these items on menu: "+ message_texts
      create_intent(project_id, "menu", menu_training,
                    [menu_response])

      #items
      for item in menu:
        training_phrases = []
        message_texts = []
        training_phrases.append("price of %s" % item)
        training_phrases.append("what will be the price of %s" % item)
        training_phrases.append("%s" %item)
        training_phrases.append("i will take  %s" % item)
        training_phrases.append("I would like to have %s" % item)
        message_texts.append("It will be $%s" % float(items_prices[item]/100))
        create_intent(project_id, item, training_phrases,
                    message_texts)

    

    
    
  except Exception as e:
    print e
    return "Error Occured while fetching merchant Data"

# Alternativly
#json which goes to dialogueflow server.
# {
#   "displayName": "bread",
#   "trainingPhrases": [
#     {
#       "type": "EXAMPLE",
#       "parts": [
#         {
#           "text": "I want some bread"
#         },
#         {
#           "text": "bread"
#         },
#         {
#           "text": "I would like some breads"
#         }
#       ]
#     }
#   ],
#   "defaultResponsePlatforms": [
#     "PLATFORM_UNSPECIFIED",
#     "FACEBOOK"
#   ],
#   "messages": [
#     {
#       "text": {
#         "text": [
#           "it will be $3"
#         ]
#       }
#     }
#   ]
# }