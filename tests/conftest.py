import pytest
from app import create_app
from app.models.data import Data

@pytest.fixture(scope='module')
def app_client_module():
    flask_app = create_app()
    test_client = flask_app.test_client()
    return test_client


@pytest.fixture(scope='module')
def new_data():
    data = Data(email='dummy@email.com', data='dummy text data')
    return data


@pytest.fixture(scope = 'function')
def process_post_body():
    file = open('tests/functional/routes/amazing_company_2.pdf', 'rb')

    headers = {
        'Content-Type': 'multipart/form-data',
        'Accept': 'application/json'
    }
    data = {
        'email': 'dummy@email.com',
        'files': file
    }
    
    return {'headers': headers, 'data': data}

