#Author: Gerard Ball
#week3accounts.py
#masking numbers

#code will prompt user to input their CC and store it in 'credit_card_number' variable
credit_card_number = input("Enter your credit card number: ")

# string masked_cc_number by concatenating four (x) followed by space and the last 4 digits of cc number using string slicing
masked_cc_number = " xxx xxx " + credit_card_number[-4:]

print("Masked credit card number:", masked_cc_number)

