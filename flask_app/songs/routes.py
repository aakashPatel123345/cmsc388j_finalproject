import base64
from io import BytesIO
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required

from .. import spotify_client
from .. forms import SearchForm, SongReviewForm, AddToFavoritesForm
from ..models import User, Review
from ..utils import current_time


songs = Blueprint("songs", __name__)

@songs.route("/", methods=["GET", "POST"])
def index():
    form =  SearchForm()
    
    if form.validate_on_submit():
        return redirect(url_for("songs.search_results", query=form.search_query.data))
    
    return render_template("index.html", form=form)


@songs.route("/search_results/<query>", methods=["GET", "POST"])
def search_results(query):
    try:
        results = spotify_client.get_music_data(query)
    except ValueError as e:
        return render_template("search_query.html", error_msg=str(e))
    
    # results is a list of dictionaries

    return render_template("search_query.html", results=results)


@songs.route("/song/<song_id>", methods=["GET", "POST"])
def song_detail(song_id):
    try:
        song = spotify_client.get_song(song_id)
    except ValueError as e:
        return render_template("song_detail.html", error_msg=str(e))
    
    reviewForm = SongReviewForm()
    if reviewForm.validate_on_submit():
        reviewForm = Review(
            commenter=current_user,
            content=reviewForm.content.data,
            date=current_time(),
            song_id=song_id,
            song_title=song.name
        )
        reviewForm.save()
        flash("Review posted successfully.", "success")
        return redirect(request.path)

    saveToFavoriteForm = AddToFavoritesForm()
    if saveToFavoriteForm.validate_on_submit():
        current_user.favorites.append(song.id)
        current_user.save()
        flash("Song added to favorites.", "success")
        return redirect(request.path)
    
    reviews = Review.objects(song_id=song_id)

    return render_template("song_detail.html", song=song, reviewForm=reviewForm, saveToFavoritesForm = saveToFavoriteForm, reviews=reviews)



@songs.route("/user/<username>")
def user_detail(username):
    user = User.objects(username=username).first()
    reviews = Review.objects(commenter=user)
    favoriteSongs = user.getSongObjects()
    return render_template("user_detail.html", user=user, reviews=reviews, favorites=favoriteSongs)