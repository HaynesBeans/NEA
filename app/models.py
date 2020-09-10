from .extensions import db
from flask_login import UserMixin
import datetime

class User(db.Model, UserMixin):

    __tablename__ = 'User'


    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    email_confirmed = db.Column(db.Boolean(), nullable=False, default=False)
    telegram_chat_id = db.Column(db.String(32), nullable=True, default=None)
    bill_groups = db.relationship('Bill_Group', backref='owner', lazy=True)


    def __repr__(self):
        return f"User('{self.email}')"


class Bill_Group(db.Model):

    __tablename__ = 'Bill_Group'


    id = db.Column(db.Integer(), primary_key=True)
    group_id = db.Column(db.String(32), unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False, default="Bill Group")
    description = db.Column(db.String(128), default="My Bill Group")
    bills = db.relationship('Bill', backref='bill_group_id', lazy=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('User.id'), nullable=False)



    def __repr__(self):
        return f"Bill_Group('{self.group_id}')"



class Bill(db.Model):

    __tablename__ = 'Bill'


    id = db.Column(db.Integer(), primary_key=True)
    bill_id = db.Column(db.String(32), unique=True, nullable=False)
    bill_job_id = db.Column(db.String(32), unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False, default="My Bill")
    description = db.Column(db.String(128), default="My Bill Description")
    recurring_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    notification_type = db.Column(db.String(16))
    # bill_group_id = db.Column(db.Integer(), db.ForeignKey('bill_group.id'), nullable=False)
    bill_group = db.Column(db.ForeignKey('Bill_Group.id'), nullable=False)
    




    def __repr__(self):
        return f"Bill('{self.bill_id} {self.bill_job_id}')"



# •	ID
# •	Username
# •	Email
# •	EmailConfirmed (Bool)
# •	Telegram Chat ID
# •	Password (Hashed)
# •	BillGroups (One-to-Many) FK
# •	Profile Picture Dir Location
# •	DarkModeEnabled (Bool)
# 2.	BillGroup Model will require the following:
# •	ID
# •	GroupID (Hashed)
# •	Name
# •	Description
# •	Bills (One-to-Many) FK
# 3.	Bill Model will require the following:
# •	ID
# •	BillID (Hashed)
# •	BillJobID (For Scheduler)
# •	Name
# •	Description
# •	Recurring UTC Time
# •	NotificationType
# 4.	Admin Model will require the following:
# •	ID
# •	Username
# •	Password
# •	TOTP Secret Key
# •	FullRights (Bool)
