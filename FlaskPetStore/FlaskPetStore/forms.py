from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class NewClothingForm(FlaskForm):
    clothingbrand = StringField('Clothing brand', validators=[DataRequired()])
    clothingtype = StringField('Clothing type', validators=[DataRequired()])
    clothingpic = StringField('Clothing picture (URL or filename)')
    clothingprice = StringField('Clothing Price')
    clothingsize = StringField('Clothing Size')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
