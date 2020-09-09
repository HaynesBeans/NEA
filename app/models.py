from .extensions import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    email_confirmed = db.Column(db.Boolean(), nullable=False, default=False)
    telegram_chat_id = db.Column(db.String(32), nullable=False, default=None)
    password = db.Column(db.String(256), nullable=False)
    bill_groups = db.relationship('BillGroup', backref='owner', lazy=True)


    def __repr__(self):
        return f"User('{self.email}')"


class BillGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.String(32), unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False, default="Bill Group")
    description = db.Column(db.String(128), default="My Bill Group")
    bills = db.relationship('Bill', backref='group', lazy=True)



    def __repr__(self):
        return f"BillGroup('{self.group_id}')"



class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bill_id = db.Column(db.String(32), unique=True, nullable=False)
    bill_job_id = db.Column(db.String(32), unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False, default="My Bill")
    description = db.Column(db.String(128), default="My Bill Description")
    recurring_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    notification_type = db.Column(db.String(16))




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
