# Code that tells you if the day is a weekday :( or a weekend :)
# Author: Gerard Ball
# Week05weekday.py

# imported datemine module to get access to datetime
import datetime

#Variable weekno and the rest used to get current time which then calls the weekday method to get the day of the week (0-6)
weekno = datetime.datetime.today().weekday()

#Monday, Tuesday, Wednesday, Thursday, Friday
if weekno < 5:

    print ("Yes, today is a Weekday - how positively wonderful...")
# weekno>5=Saturday, Sunday

#6,7 aka sat + sun 
else: 
 print ("Weekend, yessssss!")


 
