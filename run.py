import os
from app import create_app
from app.extensions import db
from app.models import Student, SystemsEng, Fisheries
from app.schema import (student_schema, students_schema,
                        systems_eng_schema, systems_engs_schema,
                        fisheries_schema, fisheriess_schema
                        )
from flask_migrate import Migrate


app = create_app(os.getenv('default') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, student_schema=student_schema, students_schema=students_schema, systems_eng_schema=systems_eng_schema, systems_engs_schema=systems_engs_schema, fisheries_schema=fisheries_schema, fisheriess_schema=fisheriess_schema)
