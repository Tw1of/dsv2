from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User, Server, Channel
from . import db
from werkzeug.security import check_password_hash, generate_password_hash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    data_user = User.query.filter_by().all()
    return render_template('base.html', data_user=data_user)

@views.route('/login')
def login():
    if User.query.count() == 0:  
        users_data = [
                ('21.04.2005', 'Tw1che.2k@gmail.com', 'Tw1', '+375445531847', generate_password_hash('1234')),
                ('22.12.2021', 'maxsidorov2017@gmail.com', 'Max', '+375296470299', generate_password_hash('1234'))
            ]
        for user_data in users_data:
                user = User( 
                    birthday=user_data[0],
                    email=user_data[1], 
                    name=user_data[2],
                    telephone=user_data[3],
                    password=user_data[4]
                            ) 
                db.session.add(user)   
                db.session.commit()
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
@login_required
def me():
    servers = current_user.joined_servers
    return render_template('@me.html', user = current_user, servers=servers)

@views.route('/servers/<int:id>')
@login_required
def server_detail(id):
    servers = current_user.joined_servers
    current_server = Server.query.filter_by(id=id).first()
    channelsText = Channel.query.filter_by(server_id=current_server.id, is_text=True).all()
    channelsVoice = Channel.query.filter_by(server_id=current_server.id, is_voice=True).all()

    first_voice_channel = channelsVoice[0] if channelsVoice else None

    # Получаем участников первого голосового канала, если он существует
    participants = first_voice_channel.members if first_voice_channel else []

    if current_server is None:
        return "Сервер не найден", 404

    return render_template(
        'server.html',
        user=current_user,
        current_server=current_server,
        servers=servers,
        channelsText=channelsText,
        channelsVoice=channelsVoice,
        participants=participants  # Передаем список участников
    )


@views.route('/chat')
def chat():
    return render_template('chat.html', user = current_user)

