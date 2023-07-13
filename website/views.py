from flask import Blueprint, render_template

views = Blueprint("views", __name__)  # doesnt have to be called views

#
@views.route('/')
def home():
    return render_template("home.html")

