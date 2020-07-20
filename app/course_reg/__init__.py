from flask import Blueprint

course_reg = Blueprint('course_reg', __name__)

from . import views 