from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError, RadioField



#Registration form details Name, email, contact, guardian/parent,  courses (Introduction to computers, Introduction to Programming, Web design 101, Databases, Application Development),  payment plan (self sponsored/ scholarship/ bursary), course fees, course units, duration of courses six months
#try to implement radio fields in registration form that will indicate course. link courses and users maybe
#student id will be implememted using a random generator and looping through existing ones

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    name = StringField('Enter your username', validators=[Required()])
    contact = StringField('Enter your phone number', validators=[Required()])
    parentGuardian = StringField("Enter your parent or guardian's full name", validators=[Required()])
    course = RadioField('Select your course', choices=[('Introduction to computers','Introduction to computers'),('Introduction to Programming','Introduction to Programming'), ('Web design 101', 'Web design 101'), ('Databases', 'Databases'), ('Application development', 'Application development')] , validators=[Required()])
    paymentPlan = RadioField('Select your payment plan', choices=[('self-sponsored','self-sponsored'),('scholarship','scholarship'), ('bursary', 'bursary')] , validators=[Required()])
    password = PasswordField('Create Password', validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators = [Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
