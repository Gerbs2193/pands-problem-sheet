#Author: Gerard Ball
#Program that creates a function that uses the Babylonian method to approximate the square root of a number
#squareroot6.py

def my_sqrt(n, tolerance=0.0001):                     #Defines my_sqrt function that takes in n square root and a tolerance of 0.0001(accuracy of approximation)
    approx = n/2                                      #Initially, the variable approx is set at half of the input n
    closer = (approx + n/approx)/2                    #Updates the approximation using the (approx + n/approx)/2 formula. 
    while abs(closer - approx) > tolerance:           #While loop that continues until the difference between the current approximation closer and the previous approximation approx is less than or equal to the tolerance value. I used the abs function to calculate the absolute value of the difference between the two approximations
        approx = closer                               #I update the previous approximation approx to be equal to the current approximation closer.
        closer = (approx + n/approx)/2                #Again, an even closer approximation is got
    return closer                                     #Finished iterating
n = int(input("Enter number: "))                      #Prompts user to enter a number and stores it in the variable n
print("Approximate square root of number:", my_sqrt(n)) #Calls my_sqrt function with the input n and prints the result as an approximation of the square root of n.