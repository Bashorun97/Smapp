from flask import Flask, request, make_response, current_app, jsonify
from . import student_reg
from app.models import Student, Course, Department
from app.schema import student_schema, course_schema
from app import db, ma
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


@student_reg.route('/student-register/<student_id>', methods=['PUT'])
@login_required
def register(current_student, student_id):
    data = request.get_json(force=True)
    student = Student.query.filter_by(student_id=student_id).first()
    if not student:
        return make_response(jsonify({'msg':'Student doesn\'t exist'}), 401)
    else:
        student.home_address = data['home_address']
        student.age = data['age']
        student.marital_status = data['marital_status']
        student.department = data['department']
        student.course = data['course']
        student.nationality = data['nationality']
        student.next_of_kin = data['next_of_kin']
        student.next_of_kin_phone = str(data['next_of_kin_phone'])
        student.next_of_kin_address = data['next_of_kin_address']
        
        dep = Department.query.filter_by(department_name=student.course).first()
        student.dep = Department.query.filter_by(department_name=data['course']).first()
        db.session.add(student)
        db.session.commit()
    return make_response(jsonify({'msg':'Successfully Registered!'}), 200)


@student_reg.route('/view-profile', methods=['GET'])
@login_required
def view_profile(current_student):
    if not current_student:
        return make_response(jsonify({'error': f'No such student found'}), 401)
    else:
        return make_response(student_schema.jsonify(current_student), 200)