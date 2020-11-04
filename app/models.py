from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

#Registration form details Name, email, contact, guardian/parent,  courses (Introduction to computers, Introduction to Programming, Web design 101, Databases, Application Development),  payment plan (self sponsored/ scholarship/ bursary), course fees, course units, duration of courses six months
#try to implement radio fields in registration form that will indicate course. link courses and users maybe
#student id will be implememted using a random generated and looping through existing ones

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int( user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    contact = db.Column(db.String(255))
    student_id = db.Column(db.String(255))
    course = db.Column(db.String(255))
    parentGuardian = db.Column(db.String(255))
    paymentPlan = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)




    def __repr__(self):
        return f'Student {self.name}'

class Courses:

    
    def __init__ (self, course_name, course_units, course_fees):
        self.course_name = course_name
        self.course_units = course_units
        self.course_fees = course_fees