from flask import Flask
from . import student_reg

@student_reg.route('/index')
def index():
    return 'hello world'