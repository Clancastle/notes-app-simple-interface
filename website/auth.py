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
        pass_p = "^(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        email_p = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"


        if email:
            pass
        elif email:
            pass

        if fname:
            pass
        elif fname:
            pass

        if re.match(pass_p, pw) == None:
            flash("Password must contain 8 characters, lowercase letter, and a digit", category="error")
            if pw != pw2:
                flash('Passwords must match.', category='error')

    else:
        pass
    data = request.form
    print(data)
    return render_template('signup.html')


"ImmutableMultiDict([('email', 'q@a'), ('fname', '2'), ('pw', '2'), ('pw2', '2')])"
"to change this immutable dict, you convert to list n change or just make another imm dict"
# GET, POST, UPDATE, PUT, DELETE: METHODS