from app import app
from flask import request
from flask import render_template
from flask import url_for
from datetime import datetime
from .extensions import db
from .extensions import queue
from .extensions import scheduler
from .models import User



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





@app.route("/login")
def login():

	home = WebDetails()




	return render_template("index.html", home=home)



@app.route("/register")
def register():

	home = WebDetails()




	return render_template("index.html", home=home)

