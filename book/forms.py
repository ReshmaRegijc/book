from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField,  SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import ValidationError
from book.models import User

class AddForm(FlaskForm):

    name = StringField("Enter name of the Book",validators=[DataRequired()])
    author = StringField("Enter Author Name",validators=[DataRequired()])
    price = IntegerField("Desired price for Book")
    submit = SubmitField("Submit")

class DeleteForm(FlaskForm):
    id = IntegerField("Enter book id")
    submit = SubmitField("Submit")

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = StringField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered!')
    

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
