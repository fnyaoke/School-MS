from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
import random
import string
from flask_login import login_user, logout_user, login_required


#email, name, contact, parentGuardian, course, paymentPlan, password, password_confirm, submit
@auth.route('/login')
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')

    title = 'tushauriane school login'


    return render_template('log_in.html', login_form = login_form, title = title)

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
     
    students_id = random.randint(0,10)
    
    if form.validate_on_submit():
        user = User(email = form.email.data, name = form.name.data, contact = form.contact.data, parentGuardian = form.parentGuardian.data, course = form.course.data, paymentPlan = form.paymentPlan.data, password = form.password.data, student_id = students_id)
        db.session.add(user)
        db.session.commit()

#        mail_message("Welcome to One Min Pitch!", "email/welcome_user", user.email, user = user)
        return redirect(url_for('auth.login'))
        title = 'New Account'


    return render_template('register.html', registration_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

