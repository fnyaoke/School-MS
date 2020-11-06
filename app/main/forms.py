from flask_wtf import FlaskForm 
from wtforms import SubmitField,TextAreaField,StringField,NumberField
from wtforms.validators import Required

class UpdateGrades(FlaskForm):
    title = StringField('Title', validators =[Required()])
    marks = NumberField('Add or Update the course',validators = [Required()])
    grade = StringField('grade', validators =[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('Add a comment,to the learner',validators = [Required()] )
    submit = SubmitField('Submit')