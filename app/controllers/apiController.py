from flask import current_app, request, jsonify
import json
import requests
import base64
from app import db
from app.controllers.errorController import AppError, catchError
from app.models.data import Data


###controller for processing pdf files 
# and communication with the Typless API
@catchError()
def process_data():
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
def save_data():
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
def get_data_all():
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
def get_data_one(id: int):
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
def delete_data_one(id: int):
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