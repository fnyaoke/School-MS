
from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Courses


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('index.html')


@main.route('/courses')
def courses():

    '''
    View root page function that returns the course page and its data
    '''
    
    return render_template('courses.html')


@main.route('/curriculars')
def curriculars():

    '''
    View root page function that returns the co curricular page and its data
    '''
    
    return render_template('co_curricular.html')



@main.route('/user/<student_id>')
def profile(student_id):
    user = User.query.filter_by(student_id = student_id).first()
#Introduction to computers,Introduction to Programming,Web design 101, Databases, Application development
    if user is None:
        abort(404)

    course_1 = Courses(course_name = 'Introduction to computers', course_units=['Definition and Computer Hardware', 'Word Processors Packages', 'Presentations using PowerPoint', 'Data analysis using Microsoft Excel'])
    course_2 = Courses(course_name = 'Introduction to Programming', course_units=['Definition and Programming Languages', 'Visual Design Basics', 'Object-Oriented Programming'])
    course_3 = Courses(course_name = 'Web design 101', course_units=['Html and CSS', 'Scripting Languages', 'Website Add-Ons', 'Web Applications'])
    course_4 = Courses(course_name = 'Databases', course_units=['Introduction to Databases', 'Types of Databses', 'Database Relationships', 'Database Applications'])

    course_fees= 'Ksh. 60,000'
    course_duration='6 months'

    if user.course == course_1.course_name :
        courses = course_1.course_units
    elif user.course == course_2.course_name:
        courses = course_2.course_units
    elif user.course == course_3.course_name:
        courses = course_3.course_units
    elif user.course == course_4.course_name:
        courses = course_4.course_units

    

    return render_template("student_portal.html", user = user, courses = courses, course_fees = course_fees, course_duration = course_duration)
