import os
from app import create_app
from app.extensions import db
from app.models import Student, Course, Department
from app.schema import (student_schema, students_schema,
                        course_schema, courses_schema,
                        department_schema, departments_schema
                        )
from flask_migrate import Migrate


app = create_app(os.getenv('default') or 'production')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app, db=db, Student=Student, Course=Course, Department=Department,
        student_schema=student_schema, students_schema=students_schema, 
        course_schema=courses_schema, department_schema=departments_schema
    )
