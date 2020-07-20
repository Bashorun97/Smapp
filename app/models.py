from app import db
import datetime as d


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(12))
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    home_address = db.Column(db.String(100))
    phone_number = db.Column(db.String(20), unique=True)
    age = db.Column(db.Integer)
    marital_status = db.Column(db.String(10))
    department = db.Column(db.String(100))
    course = db.Column(db.String(100))
    level = db.Column(db.Integer)
    last_login = db.Column(db.DateTime())
    courses_offered = db.Column(db.String(300))
    nationality = db.Column(db.String(20))
    next_of_kin = db.Column(db.String(30))
    next_of_kin_phone = db.Column(db.Integer)
    next_of_kin_address = db.Column(db.String(100))
    dept_id = db.Column(db.Integer, db.ForeignKey('department.id'))


    def compute_last_login(self):
        self.last_login = d.datetime.utcnow()


# Model declaration for Courses per student
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name  = db.Column(db.String(50))
    status = db.Column(db.String(10))
    unit = db.Column(db.Integer)
    level = db.Column(db.Integer)
    dep_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    
    @staticmethod
    def insert_courses():
        
        courses = {
        'MSM 111 Introduction to Marine Science':('C', 3, 100, 'Fisheries'),
        'MSM 211 Basic Oceanography':('C', 3, 200, 'Fisheries'),
        'MSM 520 Fish Preservation':('E', 2, 500, 'Fisheries'),
        'SSG 312 Control Theory':('C', 2, 300, 'Systems Engineering'),
        'CSC 202 Datastructures':('E', 3, 200, 'Computer Science'),
        'EEG 201 Signals and Systems':('C', 2, 200, 'Electrical Engineering'),
        'SSG 512 Expert Systems':('C', 3, 500, 'Systems Engineering'),
        'EEG 306 Circuit Theory':('C', 2, 200, 'Electrical Engineering')
        }
        for k in courses:
            course = Course.query.filter_by(course_name=k).first()
            if course is None:
                course = Course(course_name=k, status=courses[k][0], unit=courses[k][1], level=courses[k][2], dep=Department.query.filter_by(department_name=courses[k][3]).first())
            db.session.add(course) 
        db.session.commit()


# Model declarations of departments
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(50))
    students = db.relationship('Student', backref='dep')
    courses = db.relationship('Course', backref='dep')

    @staticmethod
    def insert_departments():
        departments = [
        'Fisheries', 'Electrical Engineering', 'Systems Engineering',
        'Computer Science'
        ]
        for dep in departments:
            department = Department.query.filter_by(department_name=dep).first()
            if department is None:
                department = Department(department_name=dep)
            db.session.add(department)
        db.session.commit()