#Author: Gerard Ball
#This program reads in a textfile and outputs the number of 'e's it contains. it takes the filename from an argument on the command line
#week07letterfrequency.py

#Importing the sys module, so that we can use arguments on the command line
import sys

#letterfrequency is a function, which takes the filename and a letter as input and returns the number of times the letter appears in the file. it does this on the command line using: python .\week07letterfrequency.py testing.txt e. The answer Answer: The letter e appears 24 times in the file
def letterfrequency(filename, letter):
    with open(filename, 'r') as f:
        text = f.read()
    return text.count(letter)

#Below it extracts the command-line arguments and assign them to the variables filename and letter.  sys.argv is a list containing the command-line arguments passed to the Python script. Took me longer than i care to admit figuring this out (even with the vast resources of the web)
filename = sys.argv[1]
letter = sys.argv[2][0]  # extract the first character of the second argument

#Here is calls the letterfrequency() function with the command-line arguments filename and letter and assign the result to the variable freq.
freq = letterfrequency(filename, letter)
print(f"The letter '{letter}' appears {freq} times in the file.")

'''type python .\letterfrequency.py testing.txt e into the command line with the above code and you get: The letter 'e' appears 24 times in the file
 without the command line argument input, the code will not work

 the below code will work but with no command line arguments as it simply reads the contents of the file named 'testing.txt' into a string variable, and then counts the number of occurrences of the letter 'e' in that string. The result of the count is printed to the console.
 def letterfrequency(filename, letter):
      file = open(filename, 'r')
      text = file.read()
      return text.count(letter)
print(letterfrequency('testing.txt, 'e'))
'''
