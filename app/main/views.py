from flask import render_template,request,redirect,url_for,abort,flash,session
from . import main
from flask_login import login_required,current_user
from ..models import Student,Course,Comment
from .forms import UpdateGrades,CommentForm
 
from datetime import datetime
from .email import mail_message,notification_message

from .. import db,photos
from flask.views import View,MethodView


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Main-Page'
    
    return render_template('index.html', title = title)