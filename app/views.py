from app import app
from flask import request
from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect
from datetime import datetime
from .extensions import db
from .extensions import queue
from .extensions import scheduler
from .models import User
from .forms import SignupForm, LoginForm




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
