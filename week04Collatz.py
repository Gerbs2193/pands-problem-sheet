#collatz agorithm
#Author: Gerard Ball
#collatz.py

# function def, named collatz with a number returned we want from it
def collatz(number):

    #if statement. if number modulus 2 is 0 (no remainder), then print number floor division and return it = even number
     if number %2 ==0:
      print(number//2)
      return (number //2)

   #else if first statement isnt true then number is odd
     elif number %2==1:
        result =(3*number +1)
        print (result)
        return (result)

#user input
n = input("Input positive integer: ")

#while loop. 
while n !=1:
    n = collatz(int(n))