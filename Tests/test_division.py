def test_success(test_app):
    response = test_app.get("/9/3")
    assert response.status_code == 200
    assert response.json() == {"result": "3.0"}

    response = test_app.get("/10/5")
    assert response.status_code == 200
    assert response.json() == {"result": "2.0"}

    response = test_app.get("/22/7")
    assert response.status_code == 200
    assert response.json() == {"result": "3.14"}


def test_zero_division(test_app):
    response = test_app.get("/9/0")
    assert response.status_code == 500
    assert response.json() == {"detail": "Fatal error"}


def test_type_error(test_app):
    response = test_app.get("/a/4")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "type_error.integer"

    response = test_app.get("/4/b")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "type_error.integer"

    response = test_app.get("/a/b")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "type_error.integer"

    response = test_app.get("/a/0")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "type_error.integer"

    response = test_app.get("/0/b")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "type_error.integer"
