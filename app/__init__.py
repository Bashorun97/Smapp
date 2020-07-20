import os

from flask import Flask
from .extensions import db, ma, bcrypt
from config import config


def create_app(config_type):
    app = Flask(__name__)
    app.config.from_object(config[config_type])
    config[config_type].init_app(app)
    app.config['SECRET_KEY'] = os.urandom(24)

    
    # Extension initialization
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    

    # Blueprint Registration
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')
    
    from .student_reg import student_reg as student_reg_blueprint
    app.register_blueprint(student_reg_blueprint, url_prefix='/student-reg')

    from .course_reg import course_reg as course_reg_blueprint
    app.register_blueprint(course_reg_blueprint, url_prefix='/course-reg')
    
    return app