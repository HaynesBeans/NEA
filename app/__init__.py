from flask import Flask
from flask_sslify import SSLify
from .extensions import db
from .models import User


app = Flask(__name__)
sslify = SSLify(app)

db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()


from app import views


