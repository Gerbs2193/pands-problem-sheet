#Author: Gerard Ball
#Week04collatz.py
#This programme calculates the collatz of positive integer numbers and prompts the user that they inputed a negative integer number if they have done so and that they should input a positive instead. 

def collatz(num): # define fuction collatz with num that we want from it
    sequence = []   # initialize an empty list to store the Collatz sequence
    while num != 1:
        sequence.append(num)   # add the current number to the sequence list
        if num % 2 == 0:   # if the number is even, divide it by 2
            num //= 2
    else:
            num = num * 3 + 1   # if the number is odd, multiply by 3 and add 1
            sequence.append(num)   # add the final 1 to the sequence list
    return sequence   # return the Collatz sequence as a list
num = int(input("Enter a positive integer number: "))   # prompt user for input
while num <= 0:   # loop until user enters a positive integer
    print("Invalid input. Please enter a positive integer.")
    num = int(input("Enter a positive integer number: "))
print(collatz(num))   # print the Collatz sequence for the user-provided number

    