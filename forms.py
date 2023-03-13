from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, FileField, IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Regexp

class AddDiscountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    percentage = DecimalField('Percentage', validators=[DataRequired(), NumberRange(min=0, max=100)])
    csrf_token = StringField('csrf_token')

class AddProductForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired(), NumberRange(min=0)])
    tax = DecimalField('Tax', validators=[InputRequired(), NumberRange(min=0)])
    image = FileField('Image', validators=[InputRequired()])
    # image = FileField('Image', validators=[InputRequired(), Regexp('(.*?).(jpg|png|jpeg)', message='Invalid file type.')]

