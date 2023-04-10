<style>
  h1, h2 {
    color: blue;
  }
</style>

# pands-problem-sheet
# Problems 2023

This repository is all about the weekly problem set issued by Andrew during the Programming and Scripting module in the Higher Diploma in Data Analytics course in ATU.\

Here, I will go through and explain how I solved each weekly problem sheet task, the resources I used that were essential to both my understanding of the problem being asked and how I implemented the solutions using said resources. I had next to zero experience using any programming language and, as such, i relied heavily on the extra reading Andrew supplied through the module page and the almost limitless resources online. 

## Table Of Contents
*[helloworld1.py](#helloworld1.py)
*[bank2.py](#bank2.py)
*[accounts3.py](#accounts3.py)
*[collatz4.py](#collatz4.py)
*[weekday5.py](#weekday5.py)
*[squareroot6.py](#squareroot6.py)
*[leterfrequency7.py](#letterfrequency7.py)
*[plottask8.py](#plottask8.py)
*[Conclusion](#conclusion)

## Tasks
======
## helloworld1.py <a name="helloworld1.py"></a>

## Task

Write a program that displays Hello World! when  its run. This is a simple program that prints "Hello World!" to the console within the 'Week01helloworld.py'file contained in the Pands-Problem-Sheet directory

## Usage
To run, navigate to the 'helloworld.py' file and enter the following command in the terminal:
```sh
python .\helloworld.py
```
## code
print("Hello World!)

## Output
Program prints Hello World!

## Resources and Struggles
No resources needed other than following Andrew's lead during the lab. However, I hilariously kept getting an error in the terminal as I didn't know the command in the terminal had to be the name of the file, rather than the output of Hello World! I kept typing: 
```sh
 python .\Hello World!.py 
 ```
  rather than 
  ```sh
  python .\helloworld.py. 
  ``` 
  
Embarrassing to look back on indeed.

----


## Bank2.py <a name="bank2.py"></a>

## Task

Write a program  that prompts the user to read in two money amounts in cents. Add them and print the result in euro form

## Usage
To run, navigate to the 'bank.py' file and enter the following command in the terminal:
```sh
python .\bank.py. 
```
Input 2 separate amounts in cents when instructed and await the result

## Code + Explanation
```sh
amount1 = int(input("Please enter first amount in cents"))
amount2 = int(input("Please enter second amount in cents))
answer = (amount1 + amount2)/100
print(f"The sum: €{answer}")
```

- The first line prompts the user to enter the first amount in cents using the input() function. I used int(input) as I needed to  convert the user's input (A string) into an integer, which is then assigned to the amount1 variable. If I had just used input() and tried to add both variables amounts together using this method id get an error as I cant perform a mathematical operation between a string and an integer. int(input) solves this by converting the user's input to an integer and allowing for arithmetic calculations. amount1 is the variable

- The second line same logic as first.

- Third line adds the two variable amounts together and divides the result by 100 to get the accurate decimal euro total. Then the result of the calculation is assigned to the answer variable.

- Final line I used f-string to print the value of answer in the format "€{answer}". At the point in time of doing this task, I didn't know why f-string was used and initially used: print("The sum: €" + str(answer)) as that is what I found people doing on Stack Overflow for various problems. Alas,I've been hearing using an f-string is considered more readable and convenient, as it allows you to easily include variables and expressions in your strings. I still find myself inconsistent with how I code. 

## Output
Program prints amount in euro decimal depending on user input. Example, user inputs 90 and 50 the output would be 
€1.4

## resources

1. [Python Input() Function](https://www.w3schools.com/python/ref_func_input.asp)
2. [Python int() Function](https://www.w3schools.com/python/ref_func_int.asp)
3. [Python Division Operator](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp)
4. [Python f-Strings](https://realpython.com/python-f-strings/)

I used all the above resources, specifically the w3schools int()function to do this task. I also used Stack Overflow just to see examples of people using f-strings. 

So overall, this program prompts the user to enter two amounts in cents, adds them together, converts the result to euros, and prints the result in the format "€{answer}".

----

## accounts3.py <a name="accounts3.py"></a>

## Task

Write a program that reads in a 10 character account number and outputs the account number with only the last 4 digits showing. Replace first 6 with.

## Usage

To run, navigate to 'accounts.py' file and enter the following command in the terminal:
```sh
 python .\accounts.py
 ```
 ## Code + Explanation
 ```sh
credit_card_number = input("Enter your credit card number: ")
masked_cc_number = " xxx xxx " + credit_card_number[-4:]
print("Masked credit card number:", masked_cc_number)
```

- First line of code requests the user's credit card number as  input and stores it as a string in the variable I called credit_card_number.

- Second line of code took many revisions over many weeks but eventually, from research online, combined concatenating (what I understand to be combining 2 or more strings together into 1 string) and slicing all but the last 4 digits using [-4:]. The "xxx xxx" is a string that will mask the first 6 digits of a 10 digit number. The [-4:] part of the credit_card_number string refers to a slice of the string that starts at the fourth last character and continues to the end of the string. This slice extracts the last four digits of the credit card number and concatenates it with the masked string to produce the masked credit card number. Also, you can input any length of number you wish - doesn't have to be 10 digits - and you will always get the masking of the final 4 digits. However, with this current method, the masking string only masks 6 digits. I initially had "xxxx xxxx xxxx" to simulate the usual length of a 16 standard CC, by masking the first 12 digits. From the bunker deep rabbit hole I went down researching the above solutions, I found I could also dynamically use the masking string x to cover every user inputted digit minus the last 4. I didn't 100 percent understand all of it at that time so I just stuck with the above which I did. 

- Third line In my code we simply print out the final masked CC number. We have a string called "Masked credit card number:" and a variable called masked_cc_number that has the masked credit card number. We then print the two as a single, displaying our desired masked CC number

## Output
Program masks CC number. "Enter your credit card number" - example = 012 347 1234
Masked credit card number:  xxx xxx 1234

## Resources
1. [Python String Concatenation](https://www.geeksforgeeks.org/python-string-concatenation/)
2. [Python Slice Notation - GeeksforGeeks](https://www.geeksforgeeks.org/string-slicing-in-python/)
3. [masking last 4 digits of CC](https://stackoverflow.com/questions/62304515/how-to-mask-credit-card-number-except-the-last-four-digits-using-regex)

I used all above resources tirelessly. Initially, I only used Stack Overflow and simply found an example of code from someone else and went with that. However, that only worked if the string was known like 1234567891 and then xxxxxx7891 would be the output. Not dynamic. Changed when I learned to concatenate the stings. 

So, overall, this code - using concatenation, masking and slicing - disguises the first 6 digits of a given input and only reveals the last 4

----

## collatz4.py <a name="collatz4.py"></a>

## Task

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value and, if it is even, divide it by 2, but if it is odd, multiply it by 3 and add 1. End program if current value is 1.

## Usage

To run, go to the python terminal and type:
```sh
python .\collatz.py and enter a positive integer as intructed. 
```

## Code + Explanation
```sh
def collatz(num):
    sequence = []
    while num != 1:
        sequence.append(num)
        if num % 2 == 0:
            num //= 2 
        else:
            num = num * 3 + 1
    sequence.append(num)
    return sequence
num = int(input("Enter a positive integer number: "))
while num <= 0:
    print("Detected negative integer. Please enter a positive integer number: ")
    num = int(input("Enter a positive integer number: "))
print(collatz(num))
```

- First few lines I use a non-print function for the first time called collatz with num being what we want it to do. sequence = [] was added many weeks after initial GitHub push as I eventually noticed Andrew's collatz displayed as a list whereas mine - initially - did not. This line creates an empty list called sequence which will be used to store the Collatz sequence later. This code was also my first introduction in practice to while loops and if statements. 

- The next is the formula for calculating the collatz using python. I simply looked online for the formula and how to implement it properly. The sequence.append(num) line adds the current value of num to the end of the sequence list after doing the collatz to it. So to my understanding, each time the loop runs, it adds the current value of num to the list before moving on to the next iteration. It ends when we get to 1 as the project instructs us to do. The (final) sequence is returned then. 

- However, the next part wasn't essential im sure - it was more a consequence of my love affair with rabbit holes. I wanted to issue a warning for the user if they entered a negative number. To do this, I simply introduced a while loop whereby if the num was less than 0 (<0) aka NOT a positive integer, the console would print "Detected negative integer number. Please enter a positive integer number". Then, my code prompts the user to input a positive integer number with the line num = int(input("Enter a positive integer number: ")), and assigns the new input value to num. Finished

## Output

Program performs collatz. Example - "Enter a positive integer number:"   10
[10, 5, 16, 8, 4, 2, 1]

## Resources

1. [Collatz - Stack Over Flow](https://stackoverflow.com/questions/33324432/collatz-sequence-python-3) - used this for collatz formula though my implementation uses a list and corrects user for wrong inputs as well as different coding preferences

2. [While loops - Stack Over Flow](https://stackoverflow.com/questions/36843103/while-loop-with-if-else-statement-in-python) - Used this to see many practical implementations of while loops. 

3. [W3Schools - If Statements](https://www.w3schools.com/python/gloss_python_if_statement.asp) - Used Andrew's lectures and labs but also this resource when educating myself on if statements.

4. [W3Schools - Lists](https://www.w3schools.com/python/python_lists.asp) - Went back over lists again when i realised my initial problem didnt output the sequence in a list. This link showed me how to do it. 

So, overall this code performs the collatz using the above found formula, outputs the collatz sequence.append(num) into the new list. Used while loops and if statement to complete the collatz formula. Added safeguards in the event of a user inputting a negative integer number using another while loop. 

----

## weekday5.py <a name="weekday5.py"></a>

## Task

Write a program that outputs whether or not today is a weekday. 

## Usage

To run, go to the appropriate repository or download the weekday.py file and in the terminal, type:
sh```
python .\weekday.py ``` Subsequent to this, you will be told whether it is the weekend ("Weekend, yessssss!") or a weekday (Yes, today is a Weekday - how positively wonderful..."). This is done using importing, which i will explain upon below. 

## Code + Explanation

```sh
import datetime
weekno = datetime.datetime.today().weekday()
if weekno < 5:
print ("Yes, today is a Weekday - how positively wonderful...")
else: 
 print ("Weekend, yessssss!") 
```

- This program introduced me to importing and modules. They were integral (for me) to get this program to work as instructed. So, we start by importing the datetime module. I did this after researching online and seeing that the aforementioned module is needed to give us access to the current date and time and allows us to perform operations with it. 

- The second line of code I got directly off of Stack Overflow as once I imported the datetime, I didn't know where to go from there at first. In this line, I created a variable called weekno. We get the current date and time using the datetime.today() function which then calls the weekday() method to get the day of the week as an integer between 0 (Monday) and 6 (Sunday). The resulting integer is assigned to the variable weekno. The datetime module calls 0 Monday and 6 Sunday - and everything in between as you'd expect. So this was an essential module in determining the day of the week in python. 

- We then use an if statement to determine if its a weekday and two print functions. as mentioned above, 0 represents Monday using the imported datetime module and 6 represents Sunday. So, we use the if statement to determine that the variable weekno <5: (less than 5) - then we have determined that the day is a weekday as the current day is below 5. However, if it is greater than 5 then we have determined it is a weekend as the current number is greater than 5. I print out two opposing print functions that tell the user whether they're perusing the terminal on a weekday(yay), or not (oh no).

## Output

Determines whether it is weekday, or weekend
```sh
python .\weekday.py
if <5: "(Yes, today is a Weekday - how positively wonderful...")
else: "("Weekend, yessssss!")
```

## Resources

1. [Stack over flow code used](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python)
 
2. [w3schools datetime](https://www.w3schools.com/python/python_datetime.asp)

3. [Python importing](https://www.geeksforgeeks.org/import-module-python/)

So, overall this code determines whether it is a weekday or weekend by importing the datetime module in python. 

----

## squareroot6.py <a name="squareroot6.py"></a>

## Task

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
Use Newton's approximation formula to do this. (Ended up using similar Babylonian method)

## Usage

To run, go to the appropriate repository or download the squareroot.py file and in the terminal, type:
```sh
python .\squareroot.py 
``` 
subsequent to this, you will be prompted to 'Enter number" then you will be told the "Approximate Square root of number" of what you inputted. 

## Code + Explanation

```sh
def my_sqrt(n):
    approx = n/2
    closer = (approx +n/approx)/2
    while closer != approx:
        approx = closer
        closer = (approx + n/approx)/2
        approx = closer
        closer = (approx + n/approx)/2
        approx = closer
        closer = (approx + n/approx)/2
        approx = closer
        closer = (approx + n/approx)/2
        return approx
        n=int(input("Enter number: "))
print ("Approximate square Root of Number: ", my_sqrt(n))
```
- I start here by defining a function called my_sqrt and we want it to produce the argument (n). my_sqrt was used as the function that approximates the square root of a given number using the Babylonian method. The basic formula is this: Root = 0.5 *(x +(N/x)) where x is any guess which can be assumed to be N or 1. I found online examples of this formula being used in practice and took heavy inspiration from it, specifically, one on Stack Overflow. However, as you'll soon see, my code iterates a lot more until the approximation is very accurate. 

- Then I create a variable called approx and equal it to half of the input number n aka n/2.

- I then create a variable called closer. The value of closer is calculated using the average of the current approximation approx and n/approx, which is a better approximation of the square root of n. This new value I  then assign to the closer variable.

- I then introduce a while loop. In here, the loop repeats until the current approximation closer is sufficiently close to the previous approximation approx. The != operator tests if closer and approx are not equal.

- I then update the approximations of the square root of n by setting approx to the current approximation closer and then computing a better approximation of the square root of n by taking the average of approx and n/approx. I keep iterating this until satisfied. The reason for repeating these two lines multiple times is to increase the accuracy of the approximation of the square root of n. Initially, I did this once and got the approximation square root of 81 to be 45. However, upon iterating the code several more times in the while loop, I eventually got 9.001 etc as the square root of 81. 

- I returned the finished approximation and the while loop has stopped iterating. 

- I then simply code the input and print my_sqrt(n)).

## Resources

1. [Stack over flow code example](https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm) - code realised from this example. Mine just iterates many more times for added accuracy. 

2. [Babylonian](https://www.geeksforgeeks.org/square-root-of-a-perfect-square/)

3. [iterating](https://realpython.com/python-while-loop/)

4. [my_sqrt](https://www.geeksforgeeks.org/python-math-function-sqrt/)

So, overall this program calculates an approximation of the user input using the Babylonian method and uses a function my_sqrt and while loops and iteration to achieve a relatively very accurate result. 

----

## letterfrequency7.py <a name="letterfrequency7.py"></a>
## Task

Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line. 

## Usage

To run, go to the appropriate repository or download the letterfrequency.py file and in the terminal, type:
```sh
python .\letterfrequency.py testing.txt e 
```
You will then be told how many e's appear in the above text file.

The testing.txt and e are the command line arguments that I needed to perform to complete this task. The testing.txt is the filename of the file to be searched for the letter 'e', and e is the letter to be counted in the file.

## Code + Explanation

```sh
import sys
def letterfrequency(filename, letter):
    with open(filename, 'r') as f:
        text = f.read()
    return text.count(letter)
filename = sys.argv[1]
letter = sys.argv[2][0] 
freq = letterfrequency(filename, letter)
print (f"The letter '{letter}' appears {freq} times in the file.")
```

- When the script is executed with above arguments(filename using argv[1]) and (letter as argv[2]), it will read the contents of the testing.txt file and count the number of occurrences of the letter 'e', and then print the result to the console. Simply change the letter to any other to get the count of that specific letter. I struggled with this task for than all the others but from researching and simply asking people more knowledgeable that me -  this is because the second command line argument passed to the script is assigned to the variable letter, and the count() method is called on the text string using the same variable. So whatever letter is passed as the second command line argument will be searched for in the file I randomly created 'testing.txt', and the number of occurrences of that letter will be returned. Easy, yes...

- To achieve the above - I imported the sys module as I found out that it was essential for command line arguments using argv as I will detail below. 

- I then defined my function letterfrequency and what I want from it aka the filename and the letter.

- Now the next few lines I got exclusively from Andrew and the labs as I open the filename in read mode ('r') and assign it to the variable f. I used the with statement to ensure that the file is properly closed when the block is exited. I then open the file specified by filename in read mode ('r') and assign it to the of variable f.

- I then return the number of occurrences of the character specified by letter in the string text. The count() method is used to count the occurrences - in this instance it'll be how many e's are present. The Count method is an in-built python method. 

- I then use the sys.argv arguments to allow me to do command line operations. First, I use the second command line argument (i.e. sys.argv[1]) to the variable filename. The second argument here is the texting.txt file. Unfortunately, I suffered hours upon hours of rather unenthusiastic head banging off the wall before I realised that the first argv (i.e. sys.argv(0)) is always the script's name itself aka in this instance; letterfrequency.py rather than my text file.  Oh yes, that ruined many days indeed as I kept trying to open the script itself and not the text file and got the dreaded 'File not found' error. It was quite hilarious to be fair. Regardless, filename=sys.argv[1] assigns the second command line argument - the text file - to the variable filename.

- I then assigned the first character of the third command line argument (i.e. sys.argv[2][0]) to the variable letter - letter = sys.argv[2][0]. 
I didn't really know how to do much of this task and had to heavily rely on research and similar examples and explanations. From my understanding, this particular line of code - sys.argv[2] - is the third command line argument passed to the script(letter), and is expected to be a single character. However, it is stored as a string. To get the actual character, I used [0] to get the first character of that string. So sys.argv[2][0] gets the first character of the third command line argument passed to the script plus it stores it in the variable letter. [0]was essential as without it, my script wasn't working correctly as If you omitted the [0] in sys.argv[2][0], then the value of the letter would be the entire third command line argument passed to my script (i.e., the string 'e'). This I think caused the code to look for the entire string 'e' instead of just the character 'e'. Again, i found this out by trial and error and significant online aid. 

- Lastly, I use letterfrequency function with the arguments filename and letter, and assigns the result to the variable freq.

- I then print the result with the value of the letter variable (which is passed as a command line argument as said above), as well as the value of the freq variable (which is the result of counting the occurrences of the letter in the file, e like i said above - though any letter works).

## Resources

1. [Stack over flow using count method](https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string) - used just to see ways of solving the problem (useless for command line arguments)

2. [Geeks used for educating myself on Count method](https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/) - More essential for me using the count method

3. [Stack over flow - command line arguments](https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments) - Showed me the import sys and how its used for command line arguments

4. [Geeks argv](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/) - This resource could have saved me countless idiotic hours ofstruggling. Found (eventually) that argv(0) was the script name and learned how to utilise them for command line arguments. 

5. [Python.org - ](https://docs.python.org/3/library/sys.html#sys.argv) - excellent reading on command line arguments

6. [Real strings - Strings](https://realpython.com/python-strings/) - learned to extract specific characters from a string in sys.argv[2][0] to extract the first character of the third command line argument. Very good resource.

So, overall this program calculates how many e's are in the testing.txt file by importing the sys module which allows for command line arguments (sys.argv). Once set up correctly as above - simply type:
```sh
python .\letterfrequency.py testing.txt e
```
... and you will get the following response: The letter 'e' appears 24 times in the file.

----

## plottask8.py <a name="plottask8.py"></a>
## Task

Create a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range [0, 10], 
on the one set of axes.

## Usage

To run, go to the appropriate repository or download the plottask.py file and in the terminal, type:
```sh
python .\plottask.py
```
A histogram will then be shown. 

## Code + Explanation

```sh
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
values = np.random.normal(5, 2, 1000)
x = np.linspace(0, 10, 100)
y=x**3
sns.histplot(values, bins=10, alpha=0.5, label="Histogram")
plt.plot(x, y, color = "red", label="h(x)=x^3")
plt.title("Week08plottask.py - Histogram of funtion h(x)=x^3")
plt.xlabel("Value")
plt.ylabel("Frequency or h(x)")
plt.legend()
plt.show()
```

- This code generates a histogram of the above parameters as mentioned. To achieve this - I needed to import either seaborn or just use matplotlib alone. Both of these are Python visualization libraries that are widely used in the scientific and data analysis communities. As per Andrew's lecture and lab - either work. I started off using matplotlib exclusively and got the code 'working'. However, I couldn't see the histogram no matter what I tried. I could see the plot, but no histogram. I left the computer for a while and tried importing seaborn as from what I gathered from research - it is a higher-level library built on top of Matplotlib that provides additional functionality and customization options for creating more 'aesthetically pleasing' visualizations. I went with this and realized later that the only reason my histogram was invisible earlier was because my 'bins' were set to 1 and my Alpha was set to 0. Both will result in no histogram as bins are simply the number of bars that are used to represent the data in a histogram. The bars represent a range of values in the data, and the height of each bar indicates the frequency or count of data points that fall within that range. By adjusting the number of bins - as I did from 1 to 10 - I went from seeing no histogram to seeing a completed histogram with the above plot. I also changed the alpha from 0 (which I later learned was transparent!) to 0.5 and voila - my histogram was finally viewable. This took a lot of trial and error and researching before I was happy with the end result. Seaborn - in the end - wasn't needed at all but my histogram looks slightly better with it so I left as is. 

- I started by importing the numpy library as np, seaborn library as sns and lastly, matplotlib as plt. These three were used for generating the above plot and visualizations in Python, including NumPy for numerical computations, Seaborn for higher-level visualization functions, and Matplotlib for creating and customizing plots.

- I then coded the normal distribution using the random.normal() - which I researched on w3schools -  to generate an array of 1000 random numbers drawn from a normal distribution with a mean of 5 and a standard deviation of 2, as per the task requirements. 

- Next I use NumPy's linspace() function - which I researched on numpy.org - to create an array x of 100 equally spaced points between 0 and 10. This array represents the x-axis values over which I want to plot the function y = x**3.

- I then calculate the value of y = x**3 as this is important as By creating the function h(x) = x^3, I have a mathematical function to plot on the same axes as the histogram, as the task required.  This allowed me to visualize the histogram of the normal distribution and the function h(x) = x**3 at the same time, providing a visual representation of the relationship between the two.

- The remaining lines I simply code how I want my histogram to look by using sns.histplot. I use plt.plot to plot x and y on the same axis and thats most everything. 

## Resources 

1. [Matplotlib, seaborn, hists](https://www.youtube.com/watch?v=tuDcsAxxOR8) - long but helped me understand why my hist wasn't displaying

2. [Seaborn](https://seaborn.pydata.org/tutorial.html) - A lot of this was far beyond my scope but learned the advantages seaborn has and how customizable it is. It can be as easy and difficult as you want ot to be. 

3. [Matplotlib](https://matplotlib.org/stable/users/index.html) - Used to research all the functions i would later end up using like plot(), title(), legend(), show etc

4. [Seaborn](https://www.youtube.com/watch?v=6GUZXDef2U0) - Really informative. Not that applicable really to my case as this video went far beyond what i know how to do.

5. [more seaborn reading](https://seaborn.pydata.org/generated/seaborn.histplot.html)

6. [pyplot](https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py) - Used to realise by alpha and bins mistake. Excellent for learning to format plots and hists. 

So, overall this program generates a histogram of the aforementioned requirements as soon as you type the following into the appropriate disrectory:

```sh
python .\plottask.py
```
----


## Conclusion <a name="conclusion"></a>

Firstly, I want to thank the very fortunate souls that have reached this far in and have had the great 'privilege' of reading my rather lengthy readme. I took a lot from  these tasks. To any programmer worth any salt at all, I'm sure the above tasks are mere child's play - if even that. For me, however - I struggled immensely, struggled sensationally and then to change things up - struggled some more. I panicked when i couldn't get my collatz to collatz right away; when I didn't understand how to make dynamic strings when masking CC numbers; when I had no idea what a command line argument was, never mind implement two. However, I also got a great sense of satisfaction when i - in the end - could resolve those problems through exhaustive research, discussions with my fellow classmates and examples of similar code implementations online. I am still a beginner - perhaps even that is too esteemed a term. What the above tasks have done for me is introduce me to the world of scripting and python. I've grown a fair bit from being intimidated as to how to print Hello world! to where I am now. So, I may be very low on the development ladder - but the weekly pands-problem-sheet assignments have helped me improve and learn to think logically.  