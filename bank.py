# Bank assignment that adds two (cents)amounts and prints them in human readable form
#bank.py
#Author:Gerard Ball

# variable name amount 1 then int(input) to convert string input to integer
amount1 = int(input("first amount in cents: "))

amount2 = int(input("Second amount in cents: "))

#variable answer is both inputs sum/100
answer = (amount1+amount2)/100

#print the answer
print(f"The sum: €{answer}")

