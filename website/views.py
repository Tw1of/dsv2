from flask import Blueprint, render_template
from .models import User
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    data_user = User.query.filter_by().all()
    return render_template('base.html', data_user=data_user)

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/sign')
def sign():
    month_data = [
        "Январь",
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь"
    ]
    return render_template('sign.html', month_data=month_data)

@views.route('/servers/@me')
def me():
    return render_template('@me.html')