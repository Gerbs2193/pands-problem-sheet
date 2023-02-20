# Bank assignment that adds two (cents)amounts and prints them in human readable form
#bank.py
#Author:Gerard Ball
amount1 = int(input("first amount in cents: "))
amount2 = int(input("Second amount in cents: "))
answer = (amount1+amount2)/100
print(f"The sum: €{answer}")