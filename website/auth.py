from flask import Blueprint, redirect, render_template, request, url_for

from website import views
from .models import User
from sqlalchemy import func, or_
from . import db

from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/create_acc', methods=['GET', 'POST'])
async def create_acc():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        birth_day = request.form.get('birth_day')
        birth_month = request.form.get('birth_month')
        birth_year = request.form.get('birth_year')

        is_has = User.query.filter(or_(User.email == email, User.name == name)).first()

        if not is_has:
            month_number = {
                'Январь': '01',
                'Февраль': '02',
                'Март': '03',
                'Апрель': '04',
                'Май': '05',
                'Июнь': '06',
                'Июль': '07',
                'Август': '08',
                'Сентябрь': '09',
                'Октябрь': '10',
                'Ноябрь': '11',
                'Декабрь': '12'
            }

            birth_month_numb = month_number.get(birth_month)
            
            if birth_day and birth_month_numb and birth_year:
                birthday = f'{birth_day}.{birth_month_numb}.{birth_year}'
            else:
                return "Некорректная дата рождения", 400 

            new_user = User(
            email = email,
            name = name,
            password = generate_password_hash(password),
            birthday = birthday
            )
            db.session.add(new_user)
            db.session.commit()

        return 'create_acc succes'

@auth.route('/sign_in', methods=['GET', 'POST'])
async def sign_in():
    if request.method == 'POST':
        email_telephone = request.form.get('email_telephone')
        password = str(request.form.get('password'))
        user = User.query.filter(or_(func.lower(User.email) == func.lower(email_telephone), User.telephone == email_telephone)).first()
    
        if user:
            if check_password_hash(user.password, password):
                return redirect(url_for('views.me'))
            else:
                return 'Не правильный пароль'
        else:
            return 'Почта/телефон либо пароль указаны с ошибкой'




