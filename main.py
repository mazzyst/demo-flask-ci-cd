"""ceci est un programme"""
from flask import Flask
APP = Flask(__name__)
@APP.route('/')
def hellowroldhander():
    """ceci est la fonction"""
    return 'HEllo world from Flask & VAGRANT'

if __name__ == "__main__":
    APP.run(host="0.0.0.0")
