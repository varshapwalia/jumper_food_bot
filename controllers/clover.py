import sys
from flask import Flask, Blueprint, redirect, current_app, request, session, g, abort, render_template, Response

from helper import *
from models.clover import *

clover = Blueprint('clover', __name__)


#Fetch Merchant Items from clover server
@clover.route('/merchant_search', methods=['GET','POST'])
def merchant_search():
  if request.method == 'POST':
    try:
      merchant_id = request.form['merchant_id']
      access_token = request.form['access_token']
      #helper funtion to start dumping into database
      result = find_merchant(merchant_id,access_token)
      #database/model query funtion
      merchants = fetch_merchants()
      return render_template("clover/search.html",result=result,query=merchant_id, merchants=merchants)
    except Exception as e:
      return render_template("clover/search.html",result="OOps Somethig went Wrong")
  if request.method == 'GET':
    result = " "
    merchants = fetch_merchants()
    return render_template("clover/search.html",result=result,merchants=merchants)

#showcase the item list to verify
@clover.route('/merchant_items/<mid>', methods=['GET'])
def merchant_items(mid):
  try:
    if request.method == 'GET':
      items = fetch_items(mid)
      return render_template("clover/items_list.html",items=items)
  except Exception as e:
      return render_template("clover/items_list.html")

#generate intial dialogues for the first time
@clover.route('/generate_dialogue/<mid>', methods=['GET','POST'])
def generate_dialogue(mid):
  try:
    if request.method == 'GET':
      create_dialogues(mid)
      return render_template("clover/generated.html",result = "Dialogues successfuly created!!")
  except Exception as e:
      print e
      return render_template("clover/generated.html",result="OOps Somethig went Wrong")