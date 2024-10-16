from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  
    email = db.Column(db.String(50), unique=True)
    telephone = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(12), unique=True)
    birthday = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(), nullable=False)
    servers = db.relationship('Server', backref='owner', lazy=True, cascade="all, delete-orphan")

class Server(db.Model):
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(50),  nullable=False)     
    # unique=True,
    count_of_players = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    channels = db.relationship('Channel', backref='server', lazy=True, cascade="all, delete-orphan")

class Channel(db.Model):
    __tablename__ = 'channel'
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(50), unique=True, nullable=False)
    is_text = db.Column(db.Boolean, default=False)
    is_voice = db.Column(db.Boolean, default=False)
    count_of_players = db.Column(db.Integer)
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'), nullable=False)
