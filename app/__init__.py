from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import Config
from app.controllers.errorController import error_response
"""
Main entry point of the app. 
It needs a Config object which is located in the same folder (config.py)
"""

db = SQLAlchemy() ##SQLalchemy instance for database connection and functionality

def create_app(config_class: object=Config):
    app=Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # from app.models.data import Data

    # with app.app_context():
    #     db.create_all()

    from app.routes.publicRoutes import publicRoutes
    app.register_blueprint(publicRoutes)

    from app.routes.apiRoutes import apiRoutes
    app.register_blueprint(apiRoutes)

    app.register_error_handler(404, error_response)

    return app
    
    
