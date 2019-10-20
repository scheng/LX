# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Event
from . import db
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

@main.route('/additem')
@login_required
def additem():
    return render_template('additem.html')

@main.route('/additem', methods=['POST'])
@login_required
def additem():
    t = request.form.get('time')
    route = request.form.get('route')
    stop = request.form.get('stop')
    e = Event(time = t, route = route, stop = stop)
    user = User.query.filter_by(email=current_user.email).first()
    user.events.append(e)
    db.session.add(e)
    db.session.commit()
