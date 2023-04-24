#Author: Gerard Ball
#accounts3.py
#Masking numbers

account_number = input("Enter your Account Number: ") #Code will prompt user to input their account number and store it in 'account_number' variable
masked_ac_number = " xxx xxx " + account_number[-4:]  #String masked_ac_number by concatenating (x) followed by space and the last 4 digits of ac number using string slicing
print("Masked account number:", masked_ac_number)     #Print out the masked account number by passing in the 'Masked account number' string and the value in variable 'masked_ac_number'

