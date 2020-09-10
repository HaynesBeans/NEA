from flask import Flask
from flask_sslify import SSLify
from .extensions import db
from .models import User, Bill_Group, Bill
from flask_bcrypt import Bcrypt



app = Flask(__name__)
sslify = SSLify(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config['SECRET_KEY'] = '11dac81d112effeb1c8c7a83f7a5175d' # Only for Development Testing
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcxdcoZAAAAAJzBfqVylDBORrBov25uSJPcxcXV'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcxdcoZAAAAAOwJKTxUYNbnCOl7EtK4_sJQBMy0'

db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()


from app import views


