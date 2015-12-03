from urllib.request import urlopen
import http.cookiejar
import re
import time
import webbrowser
import smtplib

# Notify that a course is available
def notify(courseURL):
  print("Seat available.")
  webbrowser.open_new(courseURL)
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("EMAIL@gmail.com", "PASSWORD")
  msg = "open seats at " + courseURL;
  server.sendmail("EMAIL@gmail.com", "EMAIL@DOMAIN.ca", msg)
  server.quit()

  
#sleep function
def sleep():
  print("Checking again in 4.5 minutes...")
  time.sleep(240)
  print("105 seconds until next check")
  time.sleep(30)




  
  
# Scan webpage for seats
def checkSeats(varCourse):

  url = varCourse;
  ubcResp = urlopen(url);
  ubcPage = ubcResp.read().decode("utf-8");

  # Search for the seat number element
  t = totalSeats.search(ubcPage);

  # Find remaining seats
  if t:
    if t.group(1) == '0':
      print ("number of seats: 0")
      return 0
    if t.group(1) == '-1':
      print ("number of seats: -1")
      return 0
    if t.group(1) == '-2':
      print ("number of seats: -2")
      return 0
    if (t.group(1) != '0' and t.group(1) != '-1' and t.group(1) != '-2'):
      return 1
  else:
    print ("Error: Can't locate number of seats.")


# Search pattern (compiled for efficiency)
totalSeats = re.compile("<TD CLASS=\"dddefault\">8</TD>(?:\n|\r\n?)<TD CLASS=\"dddefault\">(.*?)</TD>")

# Get course parameters
L13 = "https://pawnss.usask.ca/banprod/bwckschd.p_disp_listcrse?term_in=201509&subj_in=CHEM&crse_in=332&crn_in=85917"
L23 = "https://pawnss.usask.ca/banprod/bwckschd.p_disp_listcrse?term_in=201509&subj_in=CHEM&crse_in=332&crn_in=80176"
L33 = "https://pawnss.usask.ca/banprod/bwckschd.p_disp_listcrse?term_in=201509&subj_in=CHEM&crse_in=332&crn_in=87060"
test = "https://pawnss.usask.ca/banprod/bwckschd.p_disp_listcrse?term_in=201509&subj_in=ASTR&crse_in=102&crn_in=88049"

# Conditional for determining whether to register/notify
while True:
  print ("Scanning seat availablility for L13...")
  status = checkSeats(L13)
  if status == 1:
    notify(L13)
  print ("Scanning seat availablility for L23...")
  status = checkSeats(L23)
  if status == 1:
    notify(L23)
  print ("Scanning seat availablility for L33...")
  status = checkSeats(L33)
  if status == 0:
    sleep()
    continue
  if status == 1:
    notify(L33)

