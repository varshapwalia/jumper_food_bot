import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SECRET_KEY = 'thisissecret'

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True
  BASE_URL = 'http://localhost:5000/'
  # MongoDB
  MONGODB_DB = 'jumper'
  MONGODB_USERNAME = ''
  MONGODB_PASSWORD = ''
  MONGODB_HOST = ''
