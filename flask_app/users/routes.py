from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import current_user, login_required, login_user, logout_user
import base64
from io import BytesIO
from .. import bcrypt
from werkzeug.utils import secure_filename
from ..forms import RegistrationForm, LoginForm
from ..models import User

users = Blueprint("users", __name__)

@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated: 
        return redirect(url_for("songs.index"))
    
    form = RegistrationForm() 

    if request.method == "POST" and form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        user.save()
        return redirect(url_for("songs.index"))
    
    return render_template("register.html", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("songs.index"))
    
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("songs.index"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")

    return render_template("login.html", form=form)


@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("songs.index"))

def custom_404(error):
    return render_template("404.html"), 404


@users.route("/account_details", methods=["GET", "POST"])
@login_required
def account():
    return render_template("account_details.html", current_username = current_user.username)
