import sys
from flask import Flask, Blueprint, redirect, current_app, request, session, g, abort, render_template

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
  #returns the index page
  return render_template("main/index.html")