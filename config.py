import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a long string with jib jab wallygog give a dog a cone'
