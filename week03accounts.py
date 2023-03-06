#Author: Gerard Ball
#week3accounts.py
#masking numbers


#converts string input to an integer
amount = int(input("Enter Bank Account Number ending (6789)"))

# string is static as last 4 digits remind user to input their card
str = "123456789"

#returns number of chars in string
strlength = len(str)

#Hide all but last 4 digits in string
masked = strlength - 4


str = str[masked:]
print ("*" * masked + str)