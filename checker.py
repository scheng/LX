import time

from project import create_app
from project.models import Event
from project.models import User

app = create_app()
app.app_context().push()

while 1:
    print ([(User.query.get(e.user_id).email, e.stop) for e in Event.query.all()])
    print ([e.user_id for e in Event.query.filter(Event.time - 0 < 10).all()])
    time.sleep(1)
