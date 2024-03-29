# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Event
from . import db
from .finalp import p

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('phone')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('phone')
    name = request.form.get('name')
    password = request.form.get('password')
    sched = request.form.get('sched')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Phone number already exists')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), sched=sched)
    datas = p(sched)
    print (datas)
    for i, days in enumerate(datas):
        for data in days:
            if len(data) == 3:
                print ("adding events!")
                e=Event(day = i, time= data[0], route = data[1].split('-')[0], stop = data[2].split('-')[0])
                db.session.add(e)
                new_user.events.append(e)
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/change')
@login_required
def change():
    return render_template('change.html')

@auth.route('/change',methods=['POST'])
@login_required
def change_post():
    data = request.form.get('d')
    user = User.query.filter_by(email=current_user.email).first()
    user.sched = data
    db.session.commit()
    return redirect(url_for('main.profile'))
