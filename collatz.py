#Author: Gerard Ball
#Week04collatz.py
#This programme calculates the collatz of positive integer numbers and prompts the user that they inputed a negative integer number if they have done so and that they should input a positive instead. 

# defines a function called called with the argument of 'num'
def collatz(num):

  #empty list called sequence that stores the collatz numbers. Initially i simply outputting the collatz in typical vertical python orientation and only weeks later did i realise that Andrew's collatz example outputted them in a list. Oops
    sequence = []

    #while loop that goes on while num is not equal to 1
    while num != 1:

      #Adds current num to sequence list
        sequence.append(num)

        # if num is even
        if num % 2 == 0:

          #divides num by 2
            num //= 2

            #when num is odd
        else:

          #x num by 3 and add 1 and assign to new num value
            num = num * 3 + 1
    sequence.append(num)

    #returns final collatz
    return sequence

    #User prompted to enter positive integer number
num = int(input("Enter a positive integer number: "))

#while loop that goes on as long as num is negative aka <0
while num <= 0:
    print("Detected negative integer. please enter a positive integer number: ")
    num = int(input("Enter a positive integer number: "))
print(collatz(num))

    

    