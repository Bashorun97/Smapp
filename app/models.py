from app import db, ma


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
    nationality = db.Column(db.String(20))
    next_of_kin = db.Column(db.String(30))
    next_of_kin_phone = db.Column(db.Integer)
    next_of_kin_address = db.Column(db.String(100))
    dept_id = db.Column(db.Integer, db.ForeignKey('department.id'))


# Model declaration for Courses per student
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name  = db.Column(db.String(50))
    status = db.Column(db.String(10))
    unit = db.Column(db.Integer)
    #dep_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    

    @staticmethod
    def insert_courses():
        
        courses = {
        'MSM 111 Introduction to Marine Science':('C', 3),
        'MSM 211 Basic Oceanography':('C', 3),
        'MSM 520 Fish Preservation':('E', 2),
        'SSG 312 Control Theory':('C', 2),
        'CSC 202 Datastructures':('E', 3),
        'EEG 201 Signals and Systems':('C', 2),
        'SSG 512 Expert Systems':('C', 3),
        'EEG 306 Cicrcuit Theory':('C', 2)
        }

        for k,v in courses:
            course = Course.query.filter_by(course_name=k).first()
            if course is None:
                course = Course(course_name=k, status=v[0], unit=v[1])
            db.session.add(course) 
        db.session.commit()


# Model declarations of departments
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(50))
    students = db.relationship('Student', backref='dep')
    #courses = db.Column('Course', backref=)

    @staticmethod
    def insert_departments():
        DEPARTMENTS = [
        'Fisheries', 'Electrical Engineering', 'Systems Engineering',
        'Computer Science'
        ]
        for dep in DEPARTMENTS:
            department = Department.query.filter_by(department_name=dep).first()
            if department is None:
                department = Department(department_name=dep)
            db.session.add(department)
        db.session.commit()