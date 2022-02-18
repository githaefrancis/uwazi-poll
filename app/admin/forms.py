from sqlite3 import Time
from flask_wtf import FlaskForm
from sqlalchemy import DATETIME

from wtforms import SubmitField,StringField
from wtforms import DateField,TimeField,DateTimeLocalField
from wtforms.validators import InputRequired


class ElectionForm(FlaskForm):
  title=StringField('Title',validators=[InputRequired()])
  start_time=DateTimeLocalField('Start Time',format='%Y-%m-%dT%H:%M')
  end_time=DateTimeLocalField('Endtime',format='%Y-%m-%dT%H:%M')
  
  submit=SubmitField('Create')

class PostForm(FlaskForm):
  title=StringField('Title',validators=[InputRequired()])
  submit=SubmitField('Create')