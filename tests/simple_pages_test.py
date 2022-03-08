"""This test the homepage"""


#def test_request_main_menu_links(client):
    #   """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/index">Index</a>' in response.data
    assert b'<a class="nav-link" href="/github">Github</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CICD</a>' in response.data
    assert b'<a class="nav-link" href="/pythonflask">PythonFlask</a>' in response.data


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


def test_request_cicd(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CICD" in response.data


def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data


def test_request_github(client):
    """This makes the index page"""
    response = client.get("/github")
    assert response.status_code == 200
    assert b"Github" in response.data


def test_request_pythonflask(client):
    """This makes the index page"""
    response = client.get("/pythonflask")
    assert response.status_code == 200
    assert b"PythonFlask" in response.data


# def test_request_page1(client):
#  """This makes the index page"""
#    response = client.get("/index")
#    assert response.status_code == 200
#    assert b"Page 1" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
