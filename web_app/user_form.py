# coding: utf-8

from flask_wtf import Form
from wtforms import BooleanField, PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError
from models import User


class LoginForm(Form):
    username = TextField('Username',
            validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Unknown username')
            return False
        return True


class RegisterForm(Form):
    username = TextField('Username',
            validators=[DataRequired(), Length(min=3, max=32)])
    email = TextField('Email',
            validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password',
            validators=[DataRequired(), Length(min=8, max=64)])
    fullname = TextField('Fullname',
            validators=[DataRequired(), Length(min=3, max=32)])
    submit = SubmitField('Register')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username already registered")
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True