from main import app

def test_hello():
    # Create a test client using the Flask application configured for testing
    client = app.test_client()
    response = client.get('/')
    
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello world with Flask'
