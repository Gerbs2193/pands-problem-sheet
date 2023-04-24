#Code that tells you if the day is a weekday :( or a weekend :)
#Author: Gerard Ball
#weekday5.py

import datetime                                                    #Imported datemine module to get access to datetime
weekno = datetime.datetime.today().weekday()                       #Variable weekno and the rest used to get current time which then calls the weekday method to get the day of the week (0-6)
if weekno < 5:                                                     #if statement for 0-5 (weekday)aka Monday, Tuesday, Wednesday, Thursday, Friday
 print ("Yes, today is a Weekday - how positively wonderful...") 
else:                                                              
 print ("Weekend, yessssss!")                                      #Otherwise print