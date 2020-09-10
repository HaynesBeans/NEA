from app import app
from flask_bcrypt import Bcrypt
from flask import request
from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect
from datetime import datetime
from .extensions import db
from .extensions import queue
from .extensions import scheduler
from .models import User, Bill_Group, Bill
from .forms import SignupForm, LoginForm
from flask_login import login_user, current_user, logout_user

bcrypt = Bcrypt(app)




class WebDetails():

	def __init__(self):


		self.name = "Bills"
		self.description = "lorem ipsum brandon haynes the beast of the nation test test test."
		self.colour = "#444444"












@app.route("/")
def index():

	home = WebDetails()

	usertext = "Hello"



	return render_template("index.html", home=home)


@app.route("/register", methods=['GET', 'POST'])
def register():

	if current_user.is_authenticated:
		return redirect(url_for('index'))

	home = WebDetails()
	signupForm = SignupForm()

	if signupForm.validate_on_submit():

		# DO VALIDATION



		passwordHash = bcrypt.generate_password_hash(signupForm.password.data).decode('utf-8')
		user = User(username=signupForm.username.data, password=passwordHash, email=signupForm.email.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Your account has been created! ({signupForm.email.data})', 'success')
		return redirect(url_for('index'))





	return render_template("register.html", home=home, form=signupForm)





@app.route("/login", methods=['GET', 'POST'])
def login():

	if current_user.is_authenticated:
		return redirect(url_for('index'))

	home = WebDetails()
	loginForm = LoginForm()

	if loginForm.validate_on_submit():
		user = User.query.filter_by(email=loginForm.email.data).first()
		if user and bcrypt.check_password_hash(user.password, loginForm.password.data):
			login_user(user, remember=loginForm.remember.data)
			return redirect(url_for('index'))
		else:
			flash("Sign-In was Unsuccessful. Please check your email and password!", 'danger')

	return render_template("login.html", home=home, form=loginForm)




@app.route("/logout", methods=['GET', 'POST'])
def logout():
	logout_user()

	flash("Successfully Logged Out!", 'success')
	return redirect(url_for('index'))

























