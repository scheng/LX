# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, s = current_user.sched)

@main.route('/view')
@login_required
def view():
    item = ([x for x in current_user.sched.split(" ")])
    return render_template('view.html', items = item)
