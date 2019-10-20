import time

from project import create_app
from project.models import Event
from project.models import User

app = create_app()
app.app_context().push()

while 1:
    print (Event.query.all())
    time.sleep(1)
