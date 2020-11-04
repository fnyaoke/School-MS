from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User




@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/user/<student_id>')
def profile(student_id):
    user = User.query.filter_by(student_id = student_id).first()

    if user is None:
        abort(404)

    return render_template("student_portal.html", user = user)
