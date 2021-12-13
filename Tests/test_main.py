def test_root(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_hello(test_app):
    response = test_app.get("/hello/kirill")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello kirill"}
