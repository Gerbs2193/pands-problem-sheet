import datetime
weekno = datetime.datetime.today().weekday()
if weekno < 5:
    print ("Yes, today is a Weekday - how positively wonderful...")
else: 
    print ("Weekend, yessssss!")