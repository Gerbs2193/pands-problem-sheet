# Code that tells you if the day is a weekday :( or a weekend :)
# Author: Gerard Ball
# Week05weekday.py

# imported datemine module to get access to datetime
import datetime

#
weekno = datetime.datetime.today().weekday()

#Monday, Tuesday, Wednesday, Thursday, Friday
if weekno < 5:

    print ("Yes, today is a Weekday - how positively wonderful...")
# weekno>5=Saturday, Sunday

else: 
 print ("Weekend, yessssss!")
