from flask import Blueprint
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

from flask import session

# Хранение участников в сессии
user_rooms = {}

@socketio.on('join')
def on_join(data):
    username = data.get('user')
    room = data['room']

    if room not in user_rooms:
        user_rooms[room] = []

    if username in user_rooms[room]:
        emit('error_message', {'message': f'{username}, вы уже находитесь в комнате {room}.'})
        return

    user_rooms[room].append(username)
    join_room(room)

    emit('join_room_announcement', {'message': f'{username} has joined the room {room}'}, room=room)

    # Отправляем обновленный список участников
    emit('update_participants', {'participants': user_rooms[room]}, room=room)

    # Отправляем текущий список участников сразу после присоединения
    emit('current_participants', {'participants': user_rooms[room]}, room=room)


@socketio.on('leave')
def on_leave(data):
    username = data.get('user')
    room = data['room']

    # Удаляем пользователя из комнаты
    if room in user_rooms and username in user_rooms[room]:
        user_rooms[room].remove(username)
        leave_room(room)

    emit('leave_room_announcement', {'message': f'{username} has left the room {room}'}, room=room)

    # Отправляем обновленный список участников
    emit('update_participants', {'participants': user_rooms[room]}, room=room)

# Обработка SDP предложения (для видеопотока/демонстрации экрана)
@socketio.on('offer')
def handle_offer(data):
    room = data['room']
    offer = data['offer']
    emit('offer', {'offer': offer}, room=room, include_self=False)

# Обработка SDP ответа (для видеопотока/демонстрации экрана)
@socketio.on('answer')
def handle_answer(data):
    room = data['room']
    answer = data['answer']
    emit('answer', {'answer': answer}, room=room, include_self=False)

# Обработка ICE-кандидатов (для установления связи)
@socketio.on('candidate')
def handle_candidate(data):
    room = data['room']
    candidate = data['candidate']
    emit('candidate', {'candidate': candidate}, room=room, include_self=False)
