from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField, SelectField, TextAreaField#, IntegerField, DecimalField
from wtforms.fields.html5 import DateField, IntegerField, EmailField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, Optional, Regexp, ValidationError
from fuelapp.models import User


class registrationForm(FlaskForm):
    username = StringField('Username', validators =[DataRequired(), Length(min = 2, max = 25)])
    email = EmailField('E-mail', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 6, max = 30)])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), Length(min = 6, max = 30), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username is already taken')
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email is already in use')

class loginForm(FlaskForm):
    username = StringField('Username', validators =[DataRequired(), Length(min = 2, max = 25)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 6, max = 30)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class quoteForm(FlaskForm):
    gallonsRequested = IntegerField('Gallons requested: ', validators = [DataRequired(), NumberRange(min = 50, max = 3500)])
    deliveryDate = DateField('Delivery date', format = '%Y-%m-%d', validators = [DataRequired(message="You need to enter a date")])
    deliveryAddress = TextAreaField('Delivery address: ', validators = [DataRequired("Update your profile with an address")])
    rate = DecimalField("Price per Gallon:", validators = [Optional()])
    total = DecimalField("Total Amount:", validators = [Optional()])
    submit = SubmitField(label="Submit")
    calQuote = SubmitField(label="Calculate")

class profileForm(FlaskForm):
    name = StringField('Name: ', validators = [DataRequired(), Length(min=3, max =50)])
    address1 = StringField('Address 1: ', validators = [DataRequired(), Length(min =10, max = 100)])
    address2 = StringField('Address 2: ', validators = [Optional()])
    city = StringField('City: ', validators = [DataRequired(), Length(min=2, max =30)])
    state = SelectField ('State: ', validators = [DataRequired()],choices = [('TX', 'Texas'), ('CA', 'California'), ('NY', 'New York')])
    zipcode = IntegerField('Zip Code: ', validators= [DataRequired()])#, Length(min=5,max=5)
    submit = SubmitField('Submit')
