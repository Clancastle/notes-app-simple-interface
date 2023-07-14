from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)  # doesnt have to be called views

#
@views.route('/')
def home():
    return render_template("login.html")

