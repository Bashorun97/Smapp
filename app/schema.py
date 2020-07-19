# Schema declarations
from app.models import Student, SystemsEng, Fisheries
from app.extensions import ma

class StudentSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'name', 'surname', 'email', 'home_address',
            'phone_number', 'age', 'marital_status', 'department',
            'programme', 'level', 'nationality', 'next_of_kin', 'next_of_kin_phone',
            'next_of_kin_address'
        )
    
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


class SystemsEngSchema(ma.Schema):
    class Meta:
        fields = (
            'course_1', 'course_2', 'course_3', 'course_4', 'course_5',
            'course_6', 'course_7', 'course_8', 'course_9'
        )
    
systems_eng_schema = SystemsEngSchema()
systems_engs_schema = SystemsEngSchema(many=True)


class FisheriesSchema(ma.Schema):
    class Meta:
        fields = (
            'course_1', 'course_2', 'course_3', 'course_4', 'course_5',
            'course_6', 'course_7', 'course_8', 'course_9'
        )
    
fisheries_schema = FisheriesSchema()
fisheriess_schema = FisheriesSchema(many=True)