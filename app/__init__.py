from flask import Flask
from flask_sslify import SSLify
from .extensions import db
from .models import User, Bill_Group, Bill
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
sslify = SSLify(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config['SECRET_KEY'] = '11dac81d112effeb1c8c7a83f7a5175d' # Only for Development Testing
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcxdcoZAAAAAJzBfqVylDBORrBov25uSJPcxcXV' # Only for Development Testing
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcxdcoZAAAAAOwJKTxUYNbnCOl7EtK4_sJQBMy0' # Only for Development Testing

db.init_app(app)


with app.app_context():
    db.create_all()
    db.session.commit()






login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))



from app import views


