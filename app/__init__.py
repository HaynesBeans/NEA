from flask import Flask
from flask_sslify import SSLify
from flask_bcrypt import Bcrypt
from .extensions import db
from .models import User



app = Flask(__name__)
sslify = SSLify(app)
bcyrpt = Bcrypt(app)

app.config['SECRET_KEY'] = '11dac81d112effeb1c8c7a83f7a5175d' # Only for Development Testing

db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()


from app import views


