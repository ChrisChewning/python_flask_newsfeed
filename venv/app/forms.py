from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')





    #the 4 field types are classes imported from WTForms.
    #an object is created as a class variable for each one. 
    #the 1st arg is the description (or label)
    #validators arg checks field isn't empty

    
