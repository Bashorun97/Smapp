from app import db, ma


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    surname = db.Column(db.String(60))
    email = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(128))
    home_address = db.Column(db.String(128))
    phone_number = db.Column(db.String(50), unique=True)
    age = db.Column(db.Integer)
    marital_status = db.Column(db.String(50))
    department = db.Column(db.String(100))
    programme = db.Column(db.String(60))
    level = db.Column(db.Integer, default=100)
    nationality = db.Column(db.String(60))
    next_of_kin = db.Column(db.String(100))
    next_of_kin_phone = db.Column(db.Integer)
    next_of_kin_address = db.Column(db.String(100))


# Model declarations of Programmes
class SystemsEng(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_1 = db.Column(db.String(90))
    course_2 = db.Column(db.String(90))
    course_3 = db.Column(db.String(90))
    course_4 = db.Column(db.String(90))
    course_5 = db.Column(db.String(90))
    course_6 = db.Column(db.String(90))
    course_7 = db.Column(db.String(90))
    course_8 = db.Column(db.String(90))
    course_9 = db.Column(db.String(90))


class Fisheries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_1 = db.Column(db.String(90))
    course_2 = db.Column(db.String(90))
    course_3 = db.Column(db.String(90))
    course_4 = db.Column(db.String(90))
    course_5 = db.Column(db.String(90))
    course_6 = db.Column(db.String(90))
    course_7 = db.Column(db.String(90))
    course_8 = db.Column(db.String(90))
    course_9 = db.Column(db.String(90))
