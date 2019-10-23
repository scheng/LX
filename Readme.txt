LXpress

Inspiration
When classes seem to overwhelm our daily schedules, the last thing I want is running after the LX bus on a rainy evening, missing it by inches, and being stranded at Scott Hall bus stop for another 20 minutes. Should I rush out of the class, catch the upcoming bus and be one step ahead of the rush hour traffic. Or should I stay after class for some time and have my doubts clarified in the time I would have wasted strolling back and forth at the bus stop? These questions warrant answers as they hold potential to significantly transform student experience here at Rutgers.

What it does
The user only has to input his or her schedule from WebReg once at the beginning of the semester to the web application. The applet stores that data in a database and uses it to notify the user, once his/her class is over, regarding the preferred bus route, the nearest bus stop and the arrival time of the preferred bus. The notifications are in form of text messages sent to the user.

How I built it
I built a web app using flask and SQLAlchemy to enable users to log and and save their schedule information. It was hosted on heroku and I pointed a Domain.com domain (lxpress.tech) at the heroku site. The applet then uses the Transloc API to calculate the arrival times for a specific bus route to the nearest bus stop. This information is then then converted into an outgoing SMS via the Twilio API.
