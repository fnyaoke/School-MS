from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,NumberField,EmailField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    firstname = StringField('Enter your firstname',validators = [Required()])
    surname = StringField('Enter your  surname',validators = [Required()])
    lastname = StringField('Enter your last name',validators = [Required()])
    email = EmailField('Your Email Address',validators=[Required(),Email()])
    tel_no = NumberField('Enter your telephone number',validators = [Required()])
    guardian_name = StringField('Enter your guardian name',validators = [Required()])
    guardian_tel = NumberField('Enter your tel,guardian',validators = [Required()])
    guardian_email = EmailField('Your guardian Email Address',validators=[Required(),Email()])    
    postal_address = StringField('Enter your postall adress',validators=[Required()])
    physical_address =StringField('Enter where to find you,please',validators=[Required()])
    course_name = StringField('Enter the course of your choice',validators=[Required()])
    payment_plan=StringField('Enter your payment plan',validators=[Required()])
    submit = SubmitField('Sign Up')
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_admission_no(self,data_field):
        if User.query.filter_by(admission_no = data_field.data).first():
            raise ValidationError('That admission no is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    admission_no = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators =[Required()])
    submit = SubmitField('Sign In')        