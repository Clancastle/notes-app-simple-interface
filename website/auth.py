from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

# http://127.0.0.1:5000/a/ (route)

@auth.route('/login')
def login():
    return render_template('login.html')

# @auth.route('/logout')
# def logout():
#     return render_template

@auth.route('/signup')
def signup():
    return render_template('signup.html')