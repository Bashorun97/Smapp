from flask import Flask
from . import main

@main.route('/index')
def index():
    return 'hello world'