import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine
from flask_login import (
    LoginManager, 
    current_user,
    login_user,
    login_required,
    logout_user
)

from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename


from .client import SpotifyClient 

db = MongoEngine()
login_manager = LoginManager()
bcrypt = Bcrypt()


# client ID and secret  are stored in the environment variables (.env file in the current directory)
#CLIENT_ID = os.getenv("CLIENT_ID")
#CLIENT_SECRET = os.getenv("CLIENT_SECRET")
CLIENT_ID = "094f4f45e8e94cd5b9ca03a7796b1fae"
CLIENT_SECRET = "f9650f7c701f4aa1a8c0632eb3c02499"
spotify_client = SpotifyClient(CLIENT_ID, CLIENT_SECRET)
spotify_client.get_access_token()

from .users.routes import users
from .songs.routes import songs

def custom_404(error):
    return render_template("404.html"), 404

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_pyfile("config.py", silent=False)

    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(users)
    app.register_blueprint(songs)
    app.register_error_handler(404, custom_404)

    login_manager.login_view = "users.login"
    return app

