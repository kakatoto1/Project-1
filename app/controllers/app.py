"""A simple flask web app"""
from flask import Flask, render_template
from controllers.index_controller import IndexController
from werkzeug.debug import DebuggedApplication
from controllers.cicd_controller import CicdController
from controllers.github_controller import GithubController
from controllers.docker_controller import DockerController
from controllers.pythonflask_controller import PythonflaskController
#from controllers.cicd_controller import CicdController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/cicd", methods=['GET'])
def cicd_get():
    return CicdController.get()

@app.route("/github", methods=['GET'])
def github_get():
    return GithubController.get()

@app.route("/docker", methods=['GET'])
def docker_get():
    return DockerController.get()

@app.route("/pythonflask", methods=['GET'])
def pythonflask_get():
    return PythonflaskController.get()

#@app.route("/cicd", methods=['GET'])
#def cicd_get():
   # return CicdController.get()