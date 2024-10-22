from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO(app, cors_allowed_origins="*")


def create_app():
   

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12341234@localhost/sampledsdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config['SECRET_KEY'] = 'your_secret_key' 
    
    # Инициализируем компоненты
    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)  # Инициализируем SocketIO

    login_manager.login_view = 'auth.sign_in'

    from .models import User
    with app.app_context():
        db.drop_all()
        db.create_all()  

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from .views import views
    from .auth import auth
    from .chat import chat  # Импортируйте ваш новый Blueprint

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(chat, url_prefix='/')  # Регистрация вашего чата

    return app
