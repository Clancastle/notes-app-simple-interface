from flask import Blueprint, render_template

"""
authentication folder, for signing up, loging in and out. 

"""

auth = Blueprint("auth", __name__) #doesnt have to have auth name var, and auth in blueprint

# http://127.0.0.1:5000/a/ (route)

@auth.route('/login') #makes a new route(website/login), and we give that route html we made in a differnet file
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')