from ast import Pass
from flask_login import current_user

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import (
    InputRequired,
    Length, 
    Email,
    EqualTo,
    ValidationError
)

from .models import User

class SearchForm(FlaskForm):
    search_query = StringField("Query", validators=[InputRequired(), Length(min=1, max=100)])
    submit = SubmitField("Search Song")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=1, max=100)])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=100)])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user:
            raise ValidationError("Username already in use. Please choose another one.")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email already in use. Please choose another one.")
        
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=100)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=100)])
    submit = SubmitField("Sign In") 

class SongReviewForm(FlaskForm):
    content = TextAreaField("Comment", validators=[InputRequired(), Length(min=1, max=1000)])
    submit = SubmitField("Post Review")

class AddToFavoritesForm(FlaskForm):
    submit = SubmitField("Add to Favorites")