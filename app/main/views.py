from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db, photos
from ..models import User, Comment, Blog
from flask_login import login_required, current_user

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title= 'Home- Welcome to K-Blogs'
    return render_template('index.html',title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


