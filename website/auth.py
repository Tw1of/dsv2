from flask import Blueprint, render_template
from .models import User
from . import db

auth = Blueprint('auth', __name__)

# @auth.route('/')
# def cre():


#     data_user = User.query.filter_by().all()
#     return render_template('base.html', data_user=data_user)
