#Author: Gerad Ball
#program that creates a function that uses Newton's formula to approximate the square rot of a number
#week06squareroot.py

def my_sqrt(n):
    approx = n/2
    closer = (approx +n/approx)/2
    while closer != approx:
        approx = closer
        closer = (approx + n/approx)/2
        return approx
n=int(input("enter number: "))
print ("Square Root of Number: ", my_sqrt(n))