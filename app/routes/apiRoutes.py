from flask import Blueprint, Response
from app.controllers.apiController import (process_data, save_data, 
                                            get_data_all, get_data_one, 
                                            delete_data_one)


apiRoutes = Blueprint('apiRoutes', __name__, url_prefix='/api/v1/data')

#data processing endopint. Calls process_data API controller
@apiRoutes.route('/process', methods=["POST"])
def process() -> Response:
    '''
    Calls the process_data API controller and returns its response
    '''
    return process_data()

#save data endopint. Calls save_data API controller
@apiRoutes.route('/save', methods=["POST"])
def save() -> Response:
    '''
    Calls the save_data API controller and returns its response
    '''
    return save_data()

#get all records endpoint. Calls get_data_all API controller
@apiRoutes.route('/get_all', methods=["GET"])
def get_all() -> Response:
    '''
    Calls the get_data_all API controller and returns its response
    '''
    return get_data_all()

#get one record via id. Calls get_data_one API controller
@apiRoutes.route('/get/<int:id>', methods=["GET"])
def get_one(id: int) -> Response:
    '''
    Requires one positional argument (url endpoint):
        id: int
    
    Calls the get_data_one API controller with the provided id and returns its response.
    '''
    return get_data_one(id)

#delete one record via id. Calls delete_data_one API controller
@apiRoutes.route('/delete/<int:id>', methods=["DELETE"])
def delete_one(id: int) -> Response:
    '''
    Requires one positional argument (url endpoint):
        id: int
    
    Calls the delete_data_one API controller with the provided id and returns its response.
    '''
    return delete_data_one(id)

