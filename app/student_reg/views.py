from flask import Flask, request, make_response, current_app, jsonify
from . import student_reg
from app.models import Student, Course, Department
from functools import wraps
import jwt, json


def login_required(f):
    @wraps(f)
    def endpoint(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            if not token:
                return make_response(jsonify({'error':'Token is missing'}), 401)
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            current_student = Student.query.filter_by(student_id=data['id']).first()
            
            return f(current_student, *args, **kwargs)
        else:
            return make_response(jsonify({'error':'Token header not found'}))
    return endpoint


@student_reg.route('/studious')
@login_required
def study(current_student):
    return f'Studious'