import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-random-hex-for-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://awg:pass@localhost/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
