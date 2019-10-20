s = """Web Registration System
Logged in as SUNNY CHENG (193007053)Log Out
School of Arts & Sciences | Attempting 16.0 credits | Completed 55.0 credits
Choose Semester » Fall 2019
Course Lookup
Manage Registration
View / Print Schedule
PrintView: Calendar | List By Course | List By Day

THE BYRNE SEMINARS (01:090:101) Section 58 | [11133]
Tuesday	12:00 PM - 1:20 PM	SRN-112	Busch
HNRS COLLEGE FORUM (01:090:125) Section HF | [11603]
Wednesday	9:50 AM - 11:10 AM	AB-3200	College Avenue
Friday	2:50 PM - 4:10 PM	AB-3200	College Avenue
DATA STRUCTURES (01:198:112) Section 15 | [12397]
Tuesday	3:20 PM - 4:40 PM	TIL-254	Livingston
Thursday	3:20 PM - 4:40 PM	TIL-254	Livingston
Thursday	1:55 PM - 2:50 PM	TIL-253	Livingston
INTR DISCRET STRCT I (01:198:205) Section 02 | [06669]
Monday	1:40 PM - 3:00 PM	TIL-254	Livingston
Wednesday	1:40 PM - 3:00 PM	TIL-254	Livingston
Monday	10:35 AM - 11:30 AM	LSH-B115	Livingston
HONORS CALCULUS III (01:640:291) Section H1 | [00284]
Monday	5:00 PM - 6:20 PM	SEC-205	Busch
Wednesday	5:00 PM - 6:20 PM	SEC-205	Busch
Thursday	5:00 PM - 6:20 PM	SEC-205	Busch
Course material information for review and purchase for all courses: Barnes & Noble, New Brunswick, Barnes & Noble, Camden, Barnes & Noble, Newark.

For questions, comments or suggestions contact Camden Help Desk, Newark Help Desk, or New Brunswick/Piscataway Help Desk.

Visit web sites for Camden campus, Newark campus, New Brunswick/Piscataway campus, or Rutgers University.

Rutgers logo"""

def p(s):
	a = [x for x in s.split('\n') if x[:3] in ["Mon", "Tue", "Wed", "Thu", "Fri"]]
	for x in a:
		print (x.split())

p(s)
