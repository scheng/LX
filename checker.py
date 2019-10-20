import time

from project import create_app
from project.models import Event
from project.models import User
from project.TRANSLOCK import main

app = create_app()
app.app_context().push()

while 1:
#    print ([(User.query.get(e.user_id).email, e.stop) for e in Event.query.all()])
    a = ([e.user_id for e in Event.query.filter(Event.time - 0 < 10).all()])
    for e in Event.query.filter(Event.time-0 < 10).all():
        print (User.query.get(e.user_id).email, e.stop, e.route) #phone number, and two bus stops
        main(phone_number=User.query.get(e.user_id).email, buildA_=e.stop, buildB_=e.route)
    time.sleep(30)
