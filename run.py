import os
from app import create_app
# from app.extensions import db

app = create_app(os.getenv('default') or 'default')

'''
@app.shell_context_processor
def make_shell_context():
    return dict('enter_parameters_and_values')
''' 