from flask import Blueprint, render_template
from flask_socketio import SocketIO
from website import socketio

chat = Blueprint('chat', __name__)

@socketio.on('connect')
def handle_connect():
    print('User connected to auth')
    socketio.emit('user_connected', {'message': 'A user has connected to auth!'})

@socketio.on('disconnect')
def handle_disconnect():
    print('User disconnected from auth')
    socketio.emit('user_disconnected', {'message': 'A user has disconnected from auth!'})
