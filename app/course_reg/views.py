from flask import Flask, request, make_response, current_app, jsonify, render_template
from . import course_reg
from app.models import Student, Course, Department
from app.schema import student_schema, course_schema, courses_schema
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

def get_courses(student):
    level = student.level
    courses = student.dep.courses
    course_object, index = dict(), 0
    for c in courses:
        if c.level == level:
            index += 1
            course_object[index] = [c.course_name, c.status, c.unit, c.level]
    return course_object

@course_reg.route('/courses')
@login_required
def courses(current_student):
    course_object = get_courses(current_student)
    return make_response(jsonify(course_object), 200)


@course_reg.route('/course-register', methods=['PUT'])                                                                                                
@login_required
def register_course(current_student):
    data = request.get_json()
    if current_student is None:
        return make_response(jsonify({'msg':f'No such Student exists!'}))
    else:
        course_object = get_courses(current_student)
        offered_courses, index = '', 0
        course_dict = dict()
        for c in course_object:
            index += 1
            if course_object[c][1] == 'C':
                course_dict[index] = [course_object[c][0], course_object[c][2], course_object[c][1]]
        current_student.courses_offered = str(course_dict)
        db.session.commit()

    return make_response(jsonify(course_dict), 200)
