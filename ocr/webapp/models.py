from datetime import datetime
from webapp import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)

    # to override Mixin get_id() method which takes 'id' as input and we have defined the same as 'user_id'.
    def get_id(self):
        return (self.user_id)

    user_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_edited = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.user_name}','{self.email}','{self.user_created}','{self.user_edited}')"


class Plan(db.Model):
    plan_id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String, unique=True)
    plan_price = db.Column(db.NUMERIC)
    plan_img_cnt = db.Column(db.Integer)

    def __repr__(self):
        return f"Plan('{self.plan_name}','{self.plan_price}','{self.plan_img_cnt}')"


def default_function(context):
    return context.current_parameters.get('up_plan_img_cnt')


class UserPlan(db.Model):
    up_id = db.Column(db.Integer, primary_key=True)
    up_user_id = db.Column(db.Integer)
    up_plan_id = db.Column(db.Integer)
    up_plan_img_cnt = db.Column(db.Integer)
    up_uploaded = db.Column(db.Integer, default=0)
    up_remainder = db.Column(db.Integer, default=default_function)
    up_created = db.Column(db.DateTime, default=datetime.utcnow)
    up_flag = db.Column(db.Integer, default=1)
