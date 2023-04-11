# Bank assignment that adds two (cents)amounts and prints them in human readable form
#bank.py
#Author:Gerard Ball

amount1 = int(input("first amount in cents: "))
amount2 = int(input("Second amount in cents: "))
# variable sum_in_cents is both inputs sum
sum_in_cents = amount1 + amount2
# divide sum_in_cents by 100 to get sum in euros as an integer
sum_in_euros = sum_in_cents // 100
# get the remaining cents by taking the modulo of sum_in_cents and 100
cents = sum_in_cents % 100
# format the output string to display the sum in euros and cents
output_string = "The sum: €{}.{:02d}".format(sum_in_euros, cents)
# print the output string
print(output_string)
