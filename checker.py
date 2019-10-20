import time
from project import create_app
from project.models import Event
from project.models import User
from project.TRANSLOCK import main

app = create_app()
app.app_context().push()

while 1:
    date = 1
    h = time.time()%(24*3600)/3600-4 #the hour
#    print ([(User.query.get(e.user_id).email, e.stop) for e in Event.query.all()])
#    a = ([e.user_id for e in Event.query.filter(Event.time - 0 < 10).all()])
    print ("checking ", h)
    for e in Event.query.filter(Event.time - h < 0.01, Event.time-h > -0.01).all(): #date stuff here
        print (User.query.get(e.user_id).email, e.stop, e.route) #phone number, and two bus stops
        main(e.route, e.stop, phone_number=User.query.get(e.user_id).email)
    time.sleep(72)
