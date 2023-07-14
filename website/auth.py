from flask import Blueprint, render_template, request, flash
import re

"""
authentication folder, for signing up, loging in and out. 

"""

auth = Blueprint("auth", __name__) #doesnt have to have auth name var, and auth in blueprint

# http://127.0.0.1:5000/a/ (route)

@auth.route('/login', methods=['GET', 'POST']) #makes a new route(website/login), and we give that route html we made in a differnet file
def login():

    return render_template('login.html') #how to pass a variable to the front-end from the back-end

"be careful with changing stuff, sometimes it doesnt want to work."

@auth.route('/logout')
def logout():
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        fname = request.form.get('fname')
        pw = request.form.get('pw')
        pw2 = request.form.get('pw2')
        print(email, fname, pw, pw2)

        if len(fname) > 20 or fname.isdigit() or len(fname) < 3:
            flash('Email', category='error')
        elif bool(email):
            pass #not equal to regex
        elif pw:
            #not equal to regex
        elif pw != pw2:
            pass


    else:
        pass
    # data = request.form
    # print(data)
    return render_template('signup.html')


"ImmutableMultiDict([('email', 'q@a'), ('fname', '2'), ('pw', '2'), ('pw2', '2')])"
"to change this immutable dict, you convert to list n change or just make another imm dict"
# GET, POST, UPDATE, PUT, DELETE: METHODS