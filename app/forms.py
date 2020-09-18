from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import TextArea
from .models import User


class SignupForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

	email = StringField('Email', validators=[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired()])

	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

	recaptcha = RecaptchaField()

	submit = SubmitField('Register')


	def validate_email(self, email):

		user = User.query.filter_by(email=email.data).first()

		if user:
			raise ValidationError('This email is already associated with an account. Please re-enter another email.')


	def validate_username(self, username):

		user = User.query.filter_by(username=username.data).first()

		if user:
			raise ValidationError('This username is already associated with an account. Please re-enter another email.')





class LoginForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired()])

	remember = BooleanField('Remember Me')

	submit = SubmitField('Sign In')




class BillGroupForm(FlaskForm):

	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])

	description = StringField('Description', widget=TextArea(), validators=[DataRequired(), Length(min=2, max=80)])

	submit = SubmitField('Create')




class Bill(FlaskForm):

	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])

	description = StringField('Description', widget=TextArea(), validators=[DataRequired(), Length(min=2, max=80)])

	submit = SubmitField('Create')




    # id = db.Column(db.Integer(), primary_key=True)
    # group_id = db.Column(db.String(32), unique=True, nullable=False)
    # name = db.Column(db.String(32), nullable=False, default="Bill Group")
    # description = db.Column(db.String(128), default="My Bill Group")
    # bills = db.relationship('Bill', backref='bill_group_id', lazy=True)
    # user_id = db.Column(db.Integer(), db.ForeignKey('User.id'), nullable=False)








