# main.py

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Event, User
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
def additem_post():
    day = request.form.get('Day')
    t = request.form.get('Time')
    route = request.form.get('Departure')
    stop = request.form.get('Destination')
    e = Event(day = day, time = t, route = route, stop = stop)
    user = User.query.filter_by(email=current_user.email).first()
    user.events.append(e)
    db.session.add(e)
    db.session.commit()
#    d = [(e.time, e.route, e.stop) for u, e in db.session.query(User, Event).filter(user.id == Event.user_id).all()]
    d = [(e.day, e.time, e.route, e.stop) for e in Event.query.filter(user.id == Event.user_id).all()]

    return render_template('view_events.html', arr = d)

@main.route('/view_events')
@login_required
def view_events():
    user = User.query.filter_by(email=current_user.email).first()
    d = [(e.day, e.time, e.route, e.stop) for e in Event.query.filter(user.id == Event.user_id).all()]
    return render_template('view_events.html', arr = d)
