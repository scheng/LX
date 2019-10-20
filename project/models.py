# models.py

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    sched = db.Column(db.String(10000))
    events = db.relationship('Event', backref='user', lazy = 'dynamic')

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String())
    route = db.Column(db.String())
    stop = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
