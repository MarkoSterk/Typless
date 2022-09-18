import os


class Config:
    '''
    Contains all configurations for Flask app.
    '''
    SECRET_KEY = os.environ["SECRET_KEY"] ###secret key of application
    TYPLESS_API_KEY = os.environ["TYPLESS_API_KEY"] ##your Typless API key
    TYPLESS_URL = os.environ["TYPLESS_URL"] ##types API URL

    SQLALCHEMY_DATABASE_URI='sqlite:///site.db' ##local sqlite db
    SQLALCHEMY_TRACK_MODIFICATIONS = False


