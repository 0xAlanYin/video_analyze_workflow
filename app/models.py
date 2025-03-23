from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    points = db.Column(db.Integer, default=10)  # 初始积分10
    last_login_date = db.Column(db.Date)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def add_points(self, points):
        self.points += points
        db.session.commit()
        
    def deduct_points(self, points):
        if self.points >= points:
            self.points -= points
            db.session.commit()
            return True
        return False
    
    def check_and_update_daily_login(self):
        today = date.today()
        if self.last_login_date != today:
            self.last_login_date = today
            self.add_points(10)  # 每日首次登录奖励10积分
            return True
        return False

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id)) 