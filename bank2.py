# Bank assignment that adds two (cents)amounts and prints them in human readable form
#bank.py
#Author:Gerard Ball

amount1 = int(input("first amount in cents: "))   # get the first input amount in cents and convert it to an integer
amount2 = int(input("Second amount in cents: "))  # get the second input amount in cents and convert it to an integer
sum_in_cents = amount1 + amount2                     # calculate the sum of the input amounts in cents
sum_in_euros = sum_in_cents // 100                  # divide the sum_in_cents by 100 to get the sum in euros as an integer
cents = sum_in_cents % 100                           # get the remaining cents by taking the modulo of sum_in_cents and 100
output_string = "The sum: €{}.{:02d}".format(sum_in_euros, cents)  # format the output string to display the sum in euros and cents
print(output_string)                                # print the output string
