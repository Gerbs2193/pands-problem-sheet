#Author: Gerad Ball
#program that creates a function that uses Newton's formula to approximate the square root of a number
#week06squareroot.py

# defines a function 'my_sqrt' that takes argument of 'n'
def my_sqrt(n):

    #variable approx = half of 'n'. Babylonian approach to approximating a number is the square root of a number is always less than or equal to half said number. Starting point approx variable
    approx = n/2

    # calcuates new approximation of n. Average of approx and n/approx is now closer to to actual square root. This approximation is located in the variable 'closer'
    closer = (approx +n/approx)/2

    # while loop. Continues for as long as approximation closer is different from previous result
    while closer != approx:

        # inside while loop, the below lines update the vaules of approx and closer for as many iterations of loop until satisfactory result is returned. Initially, i did this only once and committed this to github. However, simply adding 3 successive iterations garners a very accurate square root. ex. 81 = 9.01 whereas before it was 45
         
        approx = closer
        closer = (approx + n/approx)/2
        approx = closer
        closer = (approx + n/approx)/2
        approx = closer
        closer = (approx + n/approx)/2
        approx = closer
        closer = (approx + n/approx)/2

        #exits loop and returns final square root calculation/approximation
        return approx
        
n=int(input("Enter number: "))
print ("Approximate square Root of Number: ", my_sqrt(n))