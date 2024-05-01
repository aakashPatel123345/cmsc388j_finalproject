from flask_login import UserMixin
from . import db, login_manager
from . import spotify_client
from datetime import datetime


class User(db.Document, UserMixin):
    username = db.StringField(required=True, unique=True, min_length=1, max_length=100)
    email = db.StringField(max_length=100, required=True, unique=True)
    password = db.StringField(max_length=100, required=True)

    # All users also have a "favorites" playlist filled with song IDs
    favorites = db.ListField(db.StringField())


    def get_id(self):
        return self.username
    
    def getSongObjects(self):
        songs = []
        for song_id in self.favorites:
            song = spotify_client.get_song(song_id)
            songs.append(song)
        return songs
    


@login_manager.user_loader
def load_user(username):
    return User.objects(username=username).first()


class Review(db.Document):
    commenter = db.ReferenceField(User)
    content = db.StringField(required = True, max_length=1000)
    date = db.StringField(required=True, default=datetime.now().strftime("%B %d, %Y at %H:%M:%S"))
    song_id = db.StringField(required=True)
    song_title = db.StringField(required=True)
