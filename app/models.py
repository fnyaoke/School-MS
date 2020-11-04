from . import db

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


    def __repr__(self):
        return f'Student {self.name}'