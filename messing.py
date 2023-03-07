credit_card_number = input("Enter your credit card number: ")
masked_cc_number = "**** **** **** " + credit_card_number[-4:]
print("Masked credit card number:", masked_cc_number)