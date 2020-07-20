# Schema declarations
from app.models import Student, Course, Department
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

class CourseSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'course_name', 'status', 'unit', 'level'
        )

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

class DepartmentSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'department_name', 'course_id'
        )

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)
