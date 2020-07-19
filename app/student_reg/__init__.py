from flask import Blueprint

student_reg = Blueprint('student_reg', __name__)

from . import views