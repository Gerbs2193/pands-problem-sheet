#Author: Gerard Ball
#This program reads in a textfile and outputs the number of 'e's it contains. it takes the filename and textfile names from arguments on the command line. Any properly inputed letter to the command line will show the user how many upper and lower case versions of said letter appear in the text file: testing.txt1. 
#letterfrequency7.py


import sys                                       #Importing sys module to gain access to command line arguments using sys.argv
def letterfrequency(filename, letter):           #defines function letter_frequency that takes two arguments: filename and letter (letterfrequency7.py) and the letter. 
    with open(filename, 'r') as f:               #Opens file filename in read mode and reads its contents into the variable text. I used the with statement here to ensure that the file is closed when the code inside it is finished.
        text = f.read()                                                   
    upper_count = text.count(letter.upper())     #This counts the number of times the letter appears in the text variable as uppercase and lowercase and stores them in the variables upper_count and lower_count.
    lower_count = text.count(letter.lower())     
    return upper_count, lower_count              #Returns the upper and lower count variables
filename = sys.argv[1]                           #Here I assign the first and second command line arguments to the filename and letter variables using sys.argv 1 and 2. 
letter = sys.argv[2]
upper_count, lower_count = letterfrequency(filename, letter) #This calls the letterfrequency function with the filename and letter variables as arguments
print(f"The letter '{letter}' appears {upper_count} times as uppercase and {lower_count} times as lowercase in the file.")