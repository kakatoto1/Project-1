"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">SOLID</a>' in response.data
    assert b'<a class="nav-link" href="/docker">AAATesting</a>' in response.data
    assert b'<a class="nav-link" href="/github">Pylint</a>' in response.data
    assert b'<a class="nav-link" href="/pythonflask">OOPS</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"SOLID" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"AAATesting" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/github")
    assert response.status_code == 200
    assert b"Pylint" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/pythonflask")
    assert response.status_code == 200
    assert b"OOPS" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
