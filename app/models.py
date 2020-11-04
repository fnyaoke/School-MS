from . import db
from werkzeug.security import generate_password_hash, check_password_hash

#Registration form details Name, email, contact, guardian/parent,  courses (Introduction to computers, Introduction to Programming, Web design 101, Databases, Application Development),  payment plan (self sponsored/ scholarship/ bursary), course fees, course units, duration of courses six months
#try to implement radio fields in registration form that will indicate course. link courses and users maybe


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    contact = db.Column(db.String(255))
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