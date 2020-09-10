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

	home = WebDetails()
	signupForm = SignupForm()

	if signupForm.validate_on_submit():

		queriedUserEmail = User.query.filter_by(email=signupForm.email.data).first()
		queriedUserUsername = User.query.filter_by(username=signupForm.username.data).first()


		if queriedUserEmail:
			flash(f'An account already exists with this email! ({signupForm.email.data})', 'danger')
			return redirect(url_for('register'))

		if queriedUserUsername:
			flash(f'An account already exists with this username! ({signupForm.username.data})', 'danger')
			return redirect(url_for('register'))

		passwordHash = bcrypt.generate_password_hash(signupForm.password.data).decode('utf-8')
		user = User(username=signupForm.username.data, password=passwordHash, email=signupForm.email.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Your account has been created! ({signupForm.email.data})', 'success')
		return redirect(url_for('index'))




	return render_template("register.html", home=home, form=signupForm)





@app.route("/login", methods=['GET', 'POST'])
def login():

	home = WebDetails()
	loginForm = LoginForm()

	if loginForm.validate_on_submit():
		return redirect(url_for('index'))




	return render_template("login.html", home=home, form=loginForm)
