import os
basedir = os.path.abspath(os.path.dirname(__file__))


#hello
class Config(object):
    # ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
