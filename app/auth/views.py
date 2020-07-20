from . import auth
from flask import Flask, request, jsonify, make_response, current_app
from app.models import Student, Course, Department 
from app.schema import (
    student_schema, students_schema, course_schema,
    courses_schema, department_schema, departments_schema
)
from app.helper import email_check
from sqlalchemy.exc import IntegrityError
from app import db, ma, bcrypt
from uuid import UUID, uuid4
import datetime as d
import jwt, json
from functools import wraps


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


@auth.route('/createaccount', methods=['POST'])
def create_account():
    data = request.get_json(force=True)
    p_hash = bcrypt.generate_password_hash(data["password"])
    new_student = Student(name=data['name'], surname=data['surname'], password=p_hash, student_id=str(uuid4()))
    db.session.add(new_student)

    if email_check(data['email']):
        try:
            new_student.email = data['email']
            db.session.flush(objects=[new_student])
        except IntegrityError:
            db.session.rollback()
            return make_response(jsonify({'msg':'Email already exists!'}), 401)
    else:
        return make_response(jsonify({'msg':'Please enter a valid email address!'}), 401)
    
    try:
        new_student.telephone = data['telephone']
        db.session.flush(objects=[new_student])
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return make_response(jsonify({'msg':'Telephone already exists!'}), 401)
    
    return make_response(jsonify({f'msg':f'Account Successfully Created! Your Student ID is {new_student.student_id}'}), 200)


@auth.route('/login', methods=['GET'])
def login():
    # get request details
    auth = request.authorization
    if not auth or not auth.username:
        return make_response(jsonfiy({'error':'Invalid auth details'}), 401)
    
    student = Student.query.filter_by(student_id=auth.username).first()
    if student:
        if bcrypt.check_password_hash(student.password, auth.password):
            token = jwt.encode({
                    'id':student.student_id,
                    'exp':d.datetime.utcnow() + d.timedelta(minutes=30)},
                    current_app.config['SECRET_KEY']   
                )
            student.compute_last_login()
            return make_response(jsonify({'token':token.decode('UTF-8')}), 200)
        else:
            return make_response({'error':'Incorrect password'}, 401)
    else:
        return make_response({'error':'No such student found'}, 401)


@auth.route('/index')
@login_required
def index(current_student):
    return make_response({'msg':'Welcome to Smapp Portal. I\'m protected'}, 200)

