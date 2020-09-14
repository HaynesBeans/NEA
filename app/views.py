from app import app
from flask_bcrypt import Bcrypt
from flask import request
from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect
from flask import request
from flask import abort
from datetime import datetime
from .extensions import db
from .extensions import queue
from .extensions import scheduler
from .models import User, Bill_Group, Bill
from .forms import SignupForm, LoginForm, BillGroupForm
from flask_login import login_user, current_user, logout_user, login_required

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
			nextPage = request.args.get('next')

			if nextPage:
				return redirect(nextPage)
			else:
				return redirect(url_for('index'))

		else:
			flash("Sign-In was Unsuccessful. Please check your email and password!", 'danger')

	return render_template("login.html", home=home, form=loginForm)




@app.route("/logout", methods=['GET', 'POST'])
def logout():
	logout_user()

	flash("Successfully Logged Out!", 'success')
	return redirect(url_for('index'))



@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
	home = WebDetails()
	
	return render_template("dashboard.html", home=home)





@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
	home = WebDetails()
	
	return render_template("index.html", home=home)




@app.route("/bill-groups", methods=['GET', 'POST'])
@login_required
def billGroups():

	print(current_user.bill_groups)

	home = WebDetails()

	page = request.args.get('page', 1, type=int)

	# billGroupsList = current_user.bill_groups.paginate(page, per_page=12)

	try:
		billGroupsList = current_user.bill_groups.paginate(page, per_page=12)
	except:
		return render_template("view_bill_groups.html", home=home, billGroups=None)


	print(billGroupsList.items)

	
	return render_template("view_bill_groups.html", home=home, billGroups=billGroupsList)



@app.route("/bills", methods=['GET', 'POST'])
@login_required
def bills():
	home = WebDetails()

	group_id = request.args.get('group_id', None, type=int)

	if group_id:

		bills = Bill.query.filter_by(bill_group=group_id, user=current_user.id).all()

		if len(bills) == 0:
			abort(403)

	else:

		bills = Bill.query.filter_by(user=current_user.id).all()

		if len(bills) == 0:
			return render_template("bills.html", home=home, bills=None)

	
	return render_template("bills.html", home=home, bills=bills)





@app.route("/bill/<int:bill_id>", methods=['GET', 'POST'])
@login_required
def bill(bill_id):
	home = WebDetails()

	bill = Bill.query.get_or_404(bill_id)

	print(bill)

	if bill.owner != current_user:
		abort(403)
	
	return render_template("bill.html", home=home)



@app.route("/bill/create", methods=['GET', 'POST'])
@login_required
def billCreate():
	home = WebDetails()

	flash("This needs Updating", 'danger')
	
	return render_template("index.html", home=home)





@app.route("/bill-group/create", methods=['GET', 'POST'])
@login_required
def billGroupCreate():
	home = WebDetails()

	billGroupForm = BillGroupForm()
	print("here at the moment")

	if billGroupForm.validate_on_submit():
		print("over here")
		bill_group = Bill_Group(name=billGroupForm.name.data, description=billGroupForm.description.data)
		db.session.add(bill_group)
		current_user.bill_groups.append(bill_group)
		db.session.commit()


		flash(f'Your Bill Group has been Created! ({billGroupForm.name.data})', 'success')
		print("here in code")
		return redirect(url_for('billGroups'))

	
	return render_template("create_bill_group.html", home=home, form=billGroupForm)

















