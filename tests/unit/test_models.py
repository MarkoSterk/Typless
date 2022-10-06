"""
Tests the Data model
"""

def test_new_data(new_data):
    """
    GIVEN a Data model
    WHEN a new Data model instance is created
    THEN check the email, data and id fields are created correctly
    """
    assert new_data.email == 'dummy@email.com'
    assert new_data.data == 'dummy text data'
