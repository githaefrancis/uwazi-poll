from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import Students

class Register(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        student = Students.query.filter_by(username=username.data).first()
        if student:
            raise ValidationError('validation Error')
    
    def validate_username(self, email):
        student = Students.query.filter_by(email=email.data).first()
        if student:
            raise ValidationError('validation Error')

class Login(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

