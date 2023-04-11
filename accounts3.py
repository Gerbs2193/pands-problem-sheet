#Author: Gerard Ball
#week3accounts.py
#masking numbers


bank_account_number = input("Enter your Bank Account Number: ") #code will prompt user to input their account number and store it in 'bank_account_number' variable
masked_ac_number = " xxx xxx " + bank_account_number[-4:] # string masked_ac_number by concatenating (x) followed by space and the last 4 digits of ac number using string slicing
print("Masked bank account number:", masked_ac_number)

