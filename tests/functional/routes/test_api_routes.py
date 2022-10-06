import json


def test_get_all(app_client_module):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/v1/data/get_all' endpoint is requested (GET)
    THEN check that the response is status_code = 200 and
    'Query completed successfully' is in the response.data object
    """
    with app_client_module:
        response = app_client_module.get('/api/v1/data/get_all')
        assert b'Query completed successfully' in response.data
        assert response.status_code == 200


def test_get_one(app_client_module):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/v1/data/get/1' endpoint is requested (GET)
    THEN check that the response is status_code = 200 and
    'Query completed successfully' is in the response.data object
    """

    with app_client_module:
        response = app_client_module.get('/api/v1/data/get/2')
        assert b'Query completed successfully' in response.data
        assert response.status_code == 200


def test_get_one_fail(app_client_module):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/v1/data/get/1000' endpoint is requested (GET)
    THEN check that the response is status_code = 404 and
    'Record with this id does not exists' is in the response.data object
    id = 1000 data model entry does not exist
    """

    with app_client_module:
        response = app_client_module.get('/api/v1/data/get/1000')
        assert b'Record with this id does not exists' in response.data
        assert response.status_code == 404


# def test_delete_one(app_client_module):
#     """
#     WORKS ONLY ONCE!
#     GIVEN a Flask application configured for testing
#     WHEN the '/api/v1/data/delete/2' endpoint is requested (DELETE)
#     THEN check that the response is status_code = 204
#     """

#     with app_client_module:
#         response = app_client_module.delete('/api/v1/data/delete/2')
#         assert response.status_code == 204

def test_delete_one_fail(app_client_module):
    """
    GIVEN a FLask application configured for testing
    WHEN the '/api/v1/data/delete/1000' endpoint is requested (DELETE)
    THEN check that the response is status_code = 404 and
    'Record with this id does not exists' is in the response.data object
    id = 1000 data model entry does not exist
    """

    with app_client_module:
        response = app_client_module.delete('/api/v1/data/delete/1000')
        assert response.status_code == 404
        assert b'Record with this id does not exists' in response.data 

####
##Can't implement without working Typless API keys
####
# def test_process_data(app_client_module, process_post_body):
#     """
#     GIVEN a FLask application configured for testing
#     WHEN the '/api/v1/data/process' endpoint is requested (POST) with file and email field
#     THEN check that the response is status_code = 200 and
#     'Invoice processed successfully.' is in the request.data object
#     """
    
#     with app_client_module:
#         response = app_client_module.post('/api/v1/data/process',
#                                         data = json.dumps(process_post_body['data']),
#                                         headers = json.dumps(process_post_body['headers']))
#         assert response.status_code == 500


def test_save_data(app_client_module):
    """
    GIVEN a FLask application configured for testing
    WHEN the '/api/v1/data/save' endpoint is requested (POST) with json payload
    THEN check that the response is status_code = 201 and
    'Data was saved successfully.' is in the request.data object
    """
    data = {
        'customer': 'dummy@email.com',
        'extracted_fields': {'data': 'some dummy text data'}
    }

    with app_client_module:
        response = app_client_module.post('/api/v1/data/save', json=data)
        assert response.status_code == 201
        assert b'Data was saved successfully.' in response.data
