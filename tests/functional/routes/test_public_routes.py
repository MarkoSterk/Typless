"""
Tests the public app routes
"""

def test_index_page_get(app_client_module):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    with app_client_module:
        response = app_client_module.get('/')
        assert response.status_code == 200
        assert b'Process invoices with Typless!' in response.data



def test_index_page_post(app_client_module):
    """
    GIVEN a Flask application configured for testing
    WHEN a post request is sent to '/'
    THEN check that a 405 status code is returned
    """

    with app_client_module:
        response = app_client_module.post('/')
        assert response.status_code == 405