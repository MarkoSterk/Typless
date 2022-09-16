from flask import Blueprint
from app.controllers.apiController import (process_data, save_data, 
                                            get_data_all, get_data_one, 
                                            delete_data_one)


apiRoutes = Blueprint('apiRoutes', __name__)

#data processing endopint. Calls process_data API controller
@apiRoutes.route('/api/v1/data/process', methods=["POST"])
def process():
    return process_data()

#save data endopint. Calls save_data API controller
@apiRoutes.route('/api/v1/data/save', methods=["POST"])
def save():
    return save_data()

#get all records endpoint. Calls get_data_all API controller
@apiRoutes.route('/api/v1/data/get_all', methods=["GET"])
def get_all():
    return get_data_all()

#get one record via id. Calls get_data_one API controller
@apiRoutes.route('/api/v1/data/get/<int:id>', methods=["GET"])
def get_one(id: int):
    return get_data_one(id)

#delete one record via id. Calls delete_data_one API controller
@apiRoutes.route('/api/v1/data/delete/<int:id>', methods=["DELETE"])
def delete_one(id: int):
    return delete_data_one(id)

