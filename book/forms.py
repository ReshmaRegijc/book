from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):

    name = StringField("Enter name of the Book",validators=[DataRequired()])
    author = StringField("Enter Author Name",validators=[DataRequired()])
    price = IntegerField("Desired price for Book")
    submit = SubmitField("Submit")

class DeleteForm(FlaskForm):
    id = IntegerField("Enter book id")
    submit = SubmitField("Submit")