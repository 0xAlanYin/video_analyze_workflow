from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    # 配置
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///video_analyze.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # 初始化扩展
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    # 设置登录视图
    login_manager.login_view = 'auth.login'
    login_manager.login_message = '请先登录'
    
    # 注册蓝图
    from .views import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
    
    # 创建数据库表
    with app.app_context():
        db.create_all()
    
    return app 