from flask import current_app, request, jsonify, Response
import json
import requests
import base64
from app import db
from app.controllers.errorController import AppError, catchError
from app.models.data import Data


###controller for processing pdf files 
# and communication with the Typless API
@catchError()
def process_data() -> Response:
    '''
    Requires a valid form submission with a (.pdf) file and email address.

    Creates a base64 file string and makes a POST request to the Typless API.

    Upon successfull processing of the pdf file by Typless
    a JSON response is generated and returned.

    Additional requirements: Typless API URL, and Typless API Key.
    '''
    file = request.files['file']
    file_name = file.filename

    base64_data = base64.b64encode(file.read()).decode('utf-8')
    file_name = file.filename

    url = current_app.config["TYPLESS_URL"]
    API_KEY = current_app.config["TYPLESS_API_KEY"]

    payload = {
        "file": base64_data,
        "file_name": file_name,
        "document_type_name": "simple-invoice",
        "customer": request.form.to_dict()['email']
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f'Token {API_KEY}'
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    response = response.json()

    return jsonify({
        'status': 'success',
        'data': response,
        'message': 'Invoice processed successfully.'
    }), 200


##saves data to the local db
@catchError()
def save_data() -> Response:
    '''
    Accepts a POST request with a JSON payload.
    Payload must contain the extracted_fields field (extracted invoice data) and customer field (email address)
    Creates a new database entry with the Data object and submits it to the database.
    Returns a JSON response.
    '''
    data = request.get_json()
    data_string = json.dumps(data['extracted_fields'])
    db_data = Data(email=data['customer'], data=data_string)

    db.session.add(db_data)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'data': db_data.to_json(),
        'message': 'Data was saved successfully.'
    }), 201


##retrives all data from local db
@catchError()
def get_data_all() -> Response:
    '''
    Queries the databse for ALL recorda.
    If no records are found it returns an AppError with 404 "No data found".

    If query is not empty it returns a JSON response with the queried data.
    
    '''
    query = Data.query.all()
    if query is None:
        return AppError('No data found.', 404, 'error')
    
    data = [d.to_json() for d in query]
    
    return jsonify({
        'status': 'success',
        'length': len(data),
        'data': data,
        'message': 'Query completed successfully'
    }), 200


#retrives one record with id
@catchError()
def get_data_one(id: int) -> Response:
    '''
    Requires one positional argument:
        id: int
    
    Queries the database for a record with the provided id.
    If no record is found it returns an AppError with 404, "Record with this id does not exist"

    If record is found a JSON response is returned.
    '''
    query = Data.query.get(id)
    if query is None:
        return AppError('Record with this id does not exists', 404, 'error')

    return jsonify({
        'status': 'success',
        'data': query.to_json(),
        'message': 'Query completed successfully'
    }), 200


#deletes record with id
@catchError()
def delete_data_one(id: int) -> Response:
    '''
    Requires one positional argument:
        id: int

    Queries the database for a record with the provided id.
    If no record is found an AppError is returned with 404 "Record with this id does not exist"

    If record if found it is deleted from the database and a 204 (NO CONTENT) response is returned.
    '''
    query = Data.query.get(id)
    if query is None:
        return AppError('Record with this id does not exists', 404, 'error')

    db.session.delete(query)
    db.session.commit()
    return jsonify({
        'status': 'success',
        'data': None,
        'message': 'Record deleted successfully'
    }), 204