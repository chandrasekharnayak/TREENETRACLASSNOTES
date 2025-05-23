import pytest
from BatchCodeData.TREENETRA_AT_15.API.FlaskApi.app import create_app# Import the create_app function

@pytest.fixture(scope="module")
def client():
    """Fixture to create a test client for the Flask app."""
    app = create_app()
    app.config['TESTING'] = True  # Enable testing mode
    with app.test_client() as client:
        yield client  # Provide the test client
