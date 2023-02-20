#Author: Gerard Ball
#week3accounts.py
#masking numbers

amount = int(input("Enter Bank Account Number ending (6789)"))
str = "123456789"
strlength = len(str)
masked = strlength - 4
slimstr = str[masked:]
print ("*" * masked + slimstr)