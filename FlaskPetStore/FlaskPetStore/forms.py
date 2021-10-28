from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class NewPetForm(FlaskForm):
    petname = StringField('Pet name', validators=[DataRequired()])
    pettype = StringField('Pet type', validators=[DataRequired()])
    petpicture = StringField('Pet picture (URL or filename)')
    petprice = StringField('Pet Price')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
