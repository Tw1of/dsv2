from flask import Blueprint, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, emit
from website import socketio

chat = Blueprint('chat', __name__)

# Обработчик подключения пользователя
@socketio.on('connect')
def handle_connect():
    print('User connected')
    emit('user_connected', {'message': 'A user has connected!'})

# Обработчик отключения пользователя
@socketio.on('disconnect')
def handle_disconnect():
    print('User disconnected')
    emit('user_disconnected', {'message': 'A user has disconnected!'})

# Обработчик создания/присоединения к комнате
@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('join_room_announcement', {'message': f'{username} has joined the room {room}'}, room=room)

# Обработчик выхода из комнаты
@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('leave_room_announcement', {'message': f'{username} has left the room {room}'}, room=room)
