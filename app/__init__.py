from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import default_exceptions
from flask_compress import Compress

from app.config import Config
from app.controllers.errorController import error_response
"""
Main entry point of the app. 
It needs a Config object which is located in the same folder (config.py)
"""

db = SQLAlchemy() ##SQLalchemy instance for database connection and functionality
compress = Compress() ##uses default settings

def create_app(config_class: object=Config):
    '''
    Takes a config object with app configurations.

    Creates Flask instance with provided configurations.

    Registers all Flask extensions, error handlers and blueprints.

    Returns FLask app instance.
    '''
    #Instatiates and configures Flask instance
    app=Flask(__name__)
    app.config.from_object(config_class)

    #Initializes all app extensions/modules
    db.init_app(app)
    compress.init_app(app)

    # from app.models.data import Data

    # with app.app_context():
    #     db.create_all()


    #imports and registers blueprints
    from app.routes.publicRoutes import publicRoutes
    app.register_blueprint(publicRoutes)

    from app.routes.apiRoutes import apiRoutes
    app.register_blueprint(apiRoutes)

    for ex in default_exceptions:
        #Registers the error_response function for all default exceptions.
        app.register_error_handler(ex, error_response)

    return app
    
    
