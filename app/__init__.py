import os

from flask import Flask
#from .extensions import db, ma, cors
from config import config


def create_app(config_type):
    app = Flask(__name__)
    app.config.from_object(config[config_type])
    config[config_type].init_app(app)
    app.config['SECRET_KEY'] = os.urandom(24)

    '''
    # Extension initialization
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    '''

    # Blueprint Registration
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')

    return app