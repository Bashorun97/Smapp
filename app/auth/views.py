from flask import Flask
from . import auth

@auth.route('/index')
def index():
    return 'hello world'