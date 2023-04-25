# pands-problem-sheet 2023

This repository is all about the weekly problem set issued by my lecturer during the Programming and Scripting module in the Higher Diploma in Data Analytics course in ATU.\

Here, I will go through and explain how I solved each weekly problem sheet task, the resources I used that were essential to both my understanding of the problem being asked and how I implemented the solutions using said resources. I will be specific as to how I solved each challenge giving references to all my inspiration - be it direct or indirect.  I will also go into how each solution can be run in practical ways to use them in the real word to solve every-day problems. I had next to zero experience using any programming language and, as such, I relied heavily on the extra reading my lecturer supplied through the module page and the almost limitless resources online. 

## Table Of Contents
- [helloworld1.py](#helloworld1.py)
- [bank2.py](#bank2.py)
- [accounts3.py](#accounts3.py)
- [collatz4.py](#collatz4.py)
- [weekday5.py](#weekday5.py)
- [squareroot6.py](#squareroot6.py)
- [leterfrequency7.py](#letterfrequency7.py)
- [plottask8.py](#plottask8.py)
- [Conclusion](#conclusion)
- [READMESources](#readmeSources)
- [Bibliography](#bibliography)
- [License](#license)

## Tasks
======

## helloworld1.py <a name="helloworld1.py"></a>

## Task
Write a program that displays Hello World! when  its run. This is a simple program that prints "Hello World!" to the console within the 'Week01helloworld.py'file contained in the Pands-Problem-Sheet repository

## Usage
To run, navigate to the 'helloworld.py1' file and enter the following command in the terminal:
```sh
python .\helloworld1.py
```
## code
```print("Hello World!)
```
## Output
Program prints Hello World!

## Resources and Struggles
No resources needed other than following my lecturer's lead during the lab. However, I hilariously kept getting an error in the terminal as I didn't know the command in the terminal had to be the name of the file, rather than the output of Hello World! I kept typing: 
```sh
 python .\Hello World!.py 
 ```
  rather than 
  ```sh
  python .\helloworld1.py. 
  ``` 
  
Embarrassing to look back on indeed.

----


## Bank2.py <a name="bank2.py"></a>

## Task
Write a program  that prompts the user to read in two money amounts in cents. Add them and print the result in euro form

## Usage
To run, navigate to the 'bank2.py' file and enter the following command in the terminal:
```sh
python .\bank2.py. 
```
Input 2 separate amounts in cents when instructed and await the result

## What is it and how can it be used
This code can be used in a wide range of scenarios where you need to add two monetary amounts and display the result in a user-friendly way. For one, it could be used in a point-of-sale system where the user needs to input the amounts of items they are purchasing and the system needs to calculate the total cost.

Another use case could be for financial applications - like budgeting tools or expense trackers - where users need to input their expenses and income in cents and see their net balance displayed in Euros or any other currency.

Overall, this code demonstrates a basic but essential programming concept that is used in many real-world applications. It shows how simple arithmetic operations, combined with input/output functions, can be used to solve practical problems and provide users with valuable information. Many practical use-cases of said code exist as the code is simple to write and can be used by companies, private citizens and budding coders alike. 

## Code + Explanation
```sh
amount1 = int(input("first amount in cents: "))                   
amount2 = int(input("Second amount in cents: "))                  
sum_in_cents = amount1 + amount2                                  
sum_in_euros = sum_in_cents // 100                                
cents = sum_in_cents % 100                                        
output_string = "The sum: €{}.{:02d}".format(sum_in_euros, cents) 
print(output_string)
```

- The first line prompts the user to enter the first amount in cents using the input() function. I used int(input) as I needed to  convert the user's input (A string) into an integer, which is then assigned to the amount1 variable. If I had just used input() and tried to add both variable amounts together using this method id get an error as I cant perform a mathematical operation between a string and an integer. int(input) solves this by converting the user's input to an integer and allowing for arithmetic calculations. amount1 is the variable

- The second line same logic as first.

- The third line I calculate the sum of the input amounts in cents. I use a variable called sum_in_cents to store the sum of the inputs. 

- I then create a new variable called sum_in_euros that is created by performing the integer division of sum_in_cents by 100 using the double slash operator // in python. sum_in_cents contains the total sum in cents, and sum_in_euros contains the total sum in Euros. There are 100 cents in one Euro so dividing the total sum in cents by 100 using integer division gives the total sum in Euros without any decimal places. Initially, I had used floats to calculate this using / - however, upon reading my lecturer's feedback I promptly changed to using integer arithmetic instead. I will detail my resources in depth and how I achieved this in the resources title below. 

- I then utilise the code  'cents = sum_in_cents % 100' to calculate the number of cents that are left over after converting the sum of amount1 and amount2 to Euros.The modulo operator - % - returns the remainder of the integer division of sum_in_cents by 100. This removes any full Euros from the total and leaves only the remaining cents, which is vital for the task. 

- Lastly, The string "The sum: €{}.{:02d}" is a format string that contains two placeholders as seen by the curly brackets. The first placeholder {} is replaced with the value of sum_in_euros, which is the integer part of the sum of amount1 and amount2 in Euros. The second placeholder {:02d} is replaced with the value of cents, which is the remainder of the sum of amount1 and amount2 after converting to Euros.
The :02d part of the second placeholder is vital as it specifies that the value of cents should be displayed with two decimal places. The d indicates that the value should be treated as an integer. For example, if sum_in_euros is 1 and cents is 2 then the output would be "The sum: €1.02". The 1 is the value of sum_in_euros and the 02 is the value of cents displayed with two decimal places. Initially, I didn't format my attempt but did so upon reading my lecturer's feedback. 



## Output
Program prints amount in euro decimal depending on user input. Example, user inputs 90 and 50 the output would be 
€1.4

## resources
1. [Python Input() Function](https://www.w3schools.com/python/ref_func_input.asp)
2. [Python int() Function](https://www.w3schools.com/python/ref_func_int.asp)
3. [Python Division Operator](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp)
4. [Python string operations](https://docs.python.org/3/library/string.html#format-specification-mini-language)
5. [Python w3schools more formatting](https://www.w3schools.com/python/ref_string_format.asp)
6. [Python // arithmetic and modulus](http://anh.cs.luc.edu/handsonPythonTutorial/integer.html)

I used all the above resources. At the beginning I used the w3schools resources on int()function to do this task. I couldn't find very similar code online - however, I found the following essential for learning how to get the python format string to construct the output message: https://www.w3schools.com/python/ref_string_format.asp. I used the w3schools page to learn how to code the "The sum: €{}.{:02d}" format line and properly format my output. I also used: http://anh.cs.luc.edu/handsonPythonTutorial/integer.html to educate myself on how to change from using floats to using integer arithmetic (//) and using modulus (%) which was key as it allowed me to display the output in both euro and cents form. 

So overall, this program prompts the user to enter two amounts in cents, adds them together, converts the result to euros, and prints the result in the format in euros and cents in decimal. 

----

## accounts3.py <a name="accounts3.py"></a>

## Task
Write a program that reads in a 10 character account number and outputs the account number with only the last 4 digits showing. Replace first 6 with.

## Usage
To run, navigate to 'accounts3.py' file and enter the following command in the terminal:
```sh
 python .\accounts3.py
 ```
 
## What is it and how can it be used
This code is used to mask or hide sensitive information like a private account number. By prompting the user to input their account number and storing it in the variable 'account_number', the code then masks the account number by replacing the first digits with "x" and displaying only the last 4 digits of the account number - thus achieving privacy. 

This is useful in scenarios where the user's account number needs to be displayed or used, but the full account number cannot be shown due to privacy concerns or security reasons. For example, when displaying account information on a receipt or invoice, or when verifying a user's identity through their account number. This code allows one to enter their full account number without displaying it on screen with masking. 

This code can be easily integrated into larger software systems or applications that require masking of sensitive data, providing an additional layer of security and privacy for users. For instance; Compliance: In certain industries like finance or healthcare, it may be required by law or industry regulations to mask or encrypt personal information like including account numbers. This code can help ensure compliance with these regulations. Or, in banking, this code is already widespread as it hides sensitive information. 

So, this code has many use cases as masking sensitive numbers is something millions of users interact with on a daily basis, without knowing how. 

 ## Code + Explanation
 ```sh
account_number = input("Enter your account number: ")
masked_ac_number = " xxx xxx " + account_number[-4:]
print("Masked Account number:", masked_ac_number)
```

- First line of code requests the user's account number as input and stores it as a string in the variable I called account_number.

- Second line of code took many revisions over many weeks but eventually, from research online, combined concatenating (what I understand to be combining 2 or more strings together into 1 string) and slicing all but the last 4 digits using [-4:]. The "xxx xxx" is a string that will mask the first 6 digits of a 10 digit number. The [-4:] part of the credit_card_number string refers to a slice of the string that starts at the fourth last character and continues to the end of the string. This slice extracts the last four digits of the account number and concatenates it with the masked string to produce the masked account number. Also, you can input any length of number you wish - doesn't have to be 10 digits - and you will always get the masking of all but the final 4 digits. However, with this current method, the masking string only masks 6 digits. I initially had "xxxx xxxx xxxx" by masking the first 12 digits. From the bunker deep rabbit hole I went down researching the above solutions, I found I could also dynamically use the masking string x to cover every user inputted digit minus the last 4. I didn't 100 percent understand all of it at that time so I just stuck with the above which masks six and leaves the last 4. Even if the user inputs a 16 digit number, for example, you'll still only see the last 4 digits.   

- Third line In my code I simply print out the final masked ac number. I have a string called "Masked Account number:" and a variable called masked_cc_number that has the account number. I then print the two as a single, displaying our desired masked ac number

## Output
Program masks ac number. "Enter your account number" - example = 012 347 1234
Masked account number:  xxx xxx 1234

## Resources
1. [Python String Concatenation](https://www.geeksforgeeks.org/python-string-concatenation/)
2. [Python Slice Notation - GeeksforGeeks](https://www.geeksforgeeks.org/string-slicing-in-python/)
3. [masking last 4 digits of CC](https://stackoverflow.com/questions/62304515/how-to-mask-credit-card-number-except-the-last-four-digits-using-regex)
4. [masking example I initially used](https://www.solveforum.com/forums/threads/solved-is-there-a-better-way-to-mask-a-credit-card-number-in-python.478573/)
5. [Stack over flow source needed to use concatenating](https://stackoverflow.com/questions/43524845/mask-a-portion-of-a-string-using-regexp)

I used all above resources tirelessly. Initially, I used a coding forum called Solve Forum and simply found an example of code from someone else and went with that - https://www.solveforum.com/forums/threads/solved-is-there-a-better-way-to-mask-a-credit-card-number-in-python.478573/. However, that only worked if the string was known like 1234567891 and then xxxxxx7891 would be the output. Not dynamic. Changed when I learned to concatenate the stings. I used this Stackoverflow example - https://stackoverflow.com/questions/43524845/mask-a-portion-of-a-string-using-regexp to learn how to dynamically mask an input and slice the end. Wouldn't have been able to finish this task the way I wanted without seeing a somewhat similar example like that source. The other resources - specifically - geeksforgeeks on concatenation and slicing added to my understanding also. 

So, overall, this code - using concatenation, masking and slicing - disguises the first 6 digits of a given input and only reveals the last 4

----

## collatz4.py <a name="collatz4.py"></a>

## Task
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value and, if it is even, divide it by 2, but if it is odd, multiply it by 3 and add 1. End program if current value is 1.

## Usage
To run, go to the python terminal and type:
```sh
python .\collatz4.py and enter a positive integer as intructed. 
```

## What is it and how can it be used
The code is used to calculate and print the Collatz sequence for a given positive integer number entered by the user. The Collatz sequence is a sequence of numbers where, starting from any positive integer, if the number is even, divide it by 2, and if the number is odd, multiply it by 3 and add 1. The sequence will continue until it reaches 1.

The practical use case of the Collatz sequence is mostly in the field of mathematics and computer science. It is often used to test algorithms and mathematical conjectures and is sometimes used as an example in introductory programming courses to teach basic control flow concepts such as loops and conditional statements - as evidenced by the simple fact that I am writing about the collatz having learned about it during a introductory programming module. The collatz has also been studied extensively in mathematics and has been the subject of many research papers and publications.

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

- First few lines I use a non-print function for the first time called collatz with num being what I want it to do. sequence = [] was added many weeks after initial GitHub push as I eventually noticed my lecturer's collatz displayed as a list whereas mine - initially - did not. This line creates an empty list called sequence which will be used to store the Collatz sequence later. This code was also my first introduction in practice to while loops and if statements. 

- The next part is the formula for calculating the collatz using python. I simply looked online for the formula and how to implement it properly. The sequence.append(num) line adds the current value of num to the end of the sequence list after doing the collatz to it. So to my understanding, each time the loop runs, it adds the current value of num to the list before moving on to the next iteration. It ends when we get to 1 as the project instructs us to do. The (final) sequence is returned then. 

- However, the next part wasn't essential I'm sure - it was more a consequence of my love affair with rabbit holes. I wanted to issue a warning for the user if they entered a negative number. To do this, I simply introduced a while loop whereby if the num was less than 0 (<0) aka NOT a positive integer, the console would print "Detected negative integer number. Please enter a positive integer number". Then, my code prompts the user to input a positive integer number with the line num = int(input("Enter a positive integer number: ")), and assigns the new input value to num. Finished

## Output
Program performs collatz. Example - "Enter a positive integer number:"   10
[10, 5, 16, 8, 4, 2, 1]

## Resources
1. [Collatz - Stack Over Flow](https://stackoverflow.com/questions/33324432/collatz-sequence-python-3) - used this for collatz formula though my implementation uses a list and corrects user for wrong inputs as well as different coding preferences

2. [While loops - Stack Over Flow](https://stackoverflow.com/questions/36843103/while-loop-with-if-else-statement-in-python) - Used this to see many practical implementations of while loops. 

3. [W3Schools - If Statements](https://www.w3schools.com/python/gloss_python_if_statement.asp) - Used my lecturer's lectures and labs but also this resource when educating myself on if statements.

4. [W3Schools - Lists](https://www.w3schools.com/python/python_lists.asp) - Went back over lists again when i realised my initial problem didnt output the sequence in a list. This link showed me how to do it. 

To start, i found the collatz formula on - https://stackoverflow.com/questions/33324432/collatz-sequence-python-3 and stuck with the bones of that. Then, i went back and realized I needed my output to look different than i initially had so used sequence = [] to achieve this. My previous source - https://stackoverflow.com/questions/33324432/collatz-sequence-python-3 also contained an example of how to output a list but it used list(collatz(user)) to convert the output of the collatz generator function into a list. I dont know anything about that and found sequence = [] easier to understand and implement. I also looked on - https://www.w3schools.com/python/python_lists.asp to learn more about lists but also seen how a couple of my fellow colleagues approached theirs. 

So, overall this code performs the collatz using the above found formula, outputs the collatz sequence.append(num) into the new list. It uses while loops and an if statement to complete the collatz formula. Added safeguards in the event of a user inputting a negative integer number using another while loop. 

----

## weekday5.py <a name="weekday5.py"></a>

## Task
Write a program that outputs whether or not today is a weekday. 

## Usage
To run, go to the appropriate repository or download the weekday5.py file and in the terminal, type:
sh```
python .\weekday5.py ``` Subsequent to this, you will be told whether it is the weekend ("Weekend, yessssss!") or a weekday (Yes, today is a Weekday - how positively wonderful..."). This is done using importing, which I will explain upon below. 

## What is it and how can it be used
This code checks whether the current day of the week is a weekday or a weekend. To achieve this, I imported the datetime module which gives me access to the necessary functions to work with dates and overall times in python. Specifically, the datetime module is needed to get the current day of the week by calling the datetime.datetime.today().weekday() method. In terms of its practical use-cases, this code has many: 

. Many businesses perform certain tasks only on weekdays, like sending emails to customers or generating reports for management. The code can be used to automate such tasks based on the current day of the week.
. in an ecommerce website, this code could be used to display different promotions depending on if its a weekday or weekend.
. In a calendar application, this code could be used to display different events depending on whether its a weekday or weekend. 
. In a time tracking use case, the code could automatically categorize entries as either weekend or weekday. 

There are almost endless examples of practical use cases. 


## Code + Explanation

```sh
import datetime
weekno = datetime.datetime.today().weekday()
if weekno < 5:
print ("Yes, today is a Weekday - how positively wonderful...")
else: 
 print ("Weekend, yessssss!") 
```

- This program introduced me to importing and modules. They were integral to get this program to work as instructed. So, we start by importing the datetime module. I did this after researching online and seeing that the aforementioned module is needed to give us access to the current date and time and allows us to perform operations with it. 

- The second line of code I got directly off of Stack Overflow as once I imported the datetime, I didn't know where to go from there at first. In this line, I created a variable called weekno. I get the current date and time using the datetime.today() function which then calls the weekday() method to get the day of the week as an integer between 0 (Monday) and 6 (Sunday). The resulting integer is assigned to the variable weekno. The datetime module calls 0 Monday and 6 Sunday - and everything in between as you'd expect. So this was an essential module in determining the day of the week in python. 

- I then use an if statement to determine if its a weekday and two print functions. as mentioned above, 0 represents Monday using the imported datetime module and 6 represents Sunday. So, I use the if statement to determine that the variable weekno <5: (less than 5) - then I have determined that the day is a weekday as the current day is below 5. However, if it is greater than 5 then I have determined it is a weekend as the current number is greater than 5. I print out two opposing print functions that tell the user whether they're perusing the terminal on a weekday(yay), or not (oh no).

## Output

Determines whether it is weekday, or weekend
```sh
python .\weekday5.py
if <5: "(Yes, today is a Weekday - how positively wonderful...")
else: "("Weekend, yessssss!")
```

## Resources

1. [Stack over flow code used](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python)
 
2. [w3schools datetime](https://www.w3schools.com/python/python_datetime.asp)

3. [Python importing](https://www.geeksforgeeks.org/import-module-python/)

I found this task easier than the tasks that follow as I had found code on Stackoverflow that matched perfectly with what my task required: - https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python. The first answer on the aforementioned link displayed using 'datetime.datetime.today().weekday()' which was used to get the day of the week as an integer value between 0 and 6, where 0 is Monday and 6 Sunday. I understood the answer on Stackoverflow and used its code for this assignment. I also looked up more about datetime using https://www.w3schools.com/python/python_datetime.asp which helped me understand the datetimne module, datetime.today() function and the weekday() method. So, overall this code determines whether it is a weekday or weekend by importing the datetime module in python. 

----

## squareroot6.py <a name="squareroot6.py"></a>

## Task
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
Use Newton's approximation formula to do this. (Ended up using similar Babylonian method)

## Usage
To run, go to the appropriate repository or download the squareroot6.py file and in the terminal, type:
```sh
python .\squareroot6.py 
``` 
subsequent to this, you will be prompted to 'Enter number" then you will be told the "Approximate Square root of number" of what you inputted. 

## What is it and how can it be used
This code uses the Babylonian algorithm to accurately approximate the square root of a positive integer without using python's in built math.sqrt function. The Babylonian method is a way to iteratively calculate the square root of a number by repeatedly averaging an initial guess and the number divided by the guess until satisfied. 
The code has many practical use cases like:

Computational geometry, engineering applications that require solving equations involving square roots, especially when you don't have access to math.sqrt. The Babylonian method could also be used in programming and software development when a high level of customisation is required for square root calculations. The math.sqrt function is going to be the 'go to' and rightfully so - its quicker and generally more accurate. However, the Babylonian algorithm allows for a custom level of accuracy and an overall very accurate approximation of the square root. Example, using math.sqrt the square root of 81 is 9. Using my above algorithm, the answer is 9.000000000004924.




## Code + Explanation
```sh
def my_sqrt(n, tolerance=0.0001):                     
    approx = n/2                                      
    closer = (approx + n/approx)/2                     
    while abs(closer - approx) > tolerance:           
        approx = closer                               
        closer = (approx + n/approx)/2                
    return closer                                     
n = float(input("Enter a positive number: "))                    
while n <= 0:                                                   
    print("Invalid input. Please enter positive integer")
    n = float(input("Enter a positive integer: "))
print("Approximate square root of number:", my_sqrt(n)) 
```
- I start here by defining a function called my_sqrt that takes in n square root and a tolerance of 0.0001. Initially, I had closer = approx iterate 10 or so times before exiting the while loop but my lecturer suggested using a tolerance in the feedback as it's much cleaner and more efficient. my_sqrt was used as the function that approximates the square root of a given number using the Babylonian method. The basic formula is this: Root = 0.5 *(x +(N/x)) where x is any guess which can be assumed to be N or 1. I found online examples of this formula being used in practice and took heavy inspiration from it, specifically, one on Stack Overflow. However, my code uses a tolerance while also ensuring that if users enter a negative integer, they'll be prompted by an error message instructing them to enter a positive number. 

- The tolerance of 0.0001 was chosen as to guarantee an accurate approximation. The next block of code uses the Babylonian method for approximating the square root of a number. It starts by setting variable approx to half of the input number. Then It calculates a new approximation for the square root which is to take the average of the current approximation and the input number divided by the current approximation. Then The abs() function is used to calculate the absolute value difference between closer and approx. This is key as closer - approx > tolerance could be negative or positive and the while loop only ends when the condition is no longer True. So, the abs function ensures that the condition is always positive and that the loop will eventually terminate once the difference between closer and approx is less than or equal to the tolerance value. Took me a while to get this working. 

- After exiting the loop and returning the final closer variable, I decided - quite late on - to do as I did on my collatz4.py program and ensure if a user enters a negative integer, they will be prompted of this error and instructed to enter a positive integer. I used the input function to get the user's input as a string and the float function to convert it to a floating-point number. Then I simply added a while loop for when n is less than 0 (aka a negative integer) to print the error message above and instruct the user to enter a positive integer in its stead. 

- I then print the output of the mysqrt function. 



## Resources
1. [Stack over flow code example](https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm) - code realised from this example. Mine just uses a tolerance for added accuracy. 

2. [Babylonian](https://www.geeksforgeeks.org/square-root-of-a-perfect-square/)

3. [iterating](https://realpython.com/python-while-loop/)

4. [my_sqrt](https://www.geeksforgeeks.org/python-math-function-sqrt/)

5. [abs](https://realpython.com/python-absolute-value/)

6. [Python tolerance](https://buildmedia.readthedocs.org/media/pdf/python-tolerance/latest/python-tolerance.pdf)

To achieve the above code, I used this example on Stackoverflow - (https://www.geeksforgeeks.org/square-root-of-a-perfect-square/). This example provided me with the crux of the babylonian formula used to calculate the approximation. I then used this - https://buildmedia.readthedocs.org/media/pdf/python-tolerance/latest/python-tolerance.pdf resource to understand what a tolerance was as before the feedback I received, I was unsure how it would be better than my previous code. There was no code online that helped with the tolerance much, but the build the docs resource I just listed made me aware that setting the tolerance to as close to 0, but not zero as this could either take too long to exit the while loop and lastly, depending on the algorithm itself, may never leave the while loop. 0.0001 was chosen for this same reason. 

So, overall this program calculates an approximation of the user input using the Babylonian method and uses a function my_sqrt and while loops and iteration to achieve a very accurate result. 

----

## letterfrequency7.py <a name="letterfrequency7.py"></a>

## Task
Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line. 

## Usage
To run, go to the appropriate repository or download the letterfrequency7.py file and in the terminal, type:
```sh
python .\letterfrequency7.py testing.txt1 e 
```
You will then be told how many e's appear in the above text file.

The testing.txt and e are the command line arguments that I needed to perform to complete this task. The testing.txt1 is the filename of the file to be searched for the letter 'e', and e is the letter to be counted in the file.

## What is it and how can it be used
This code reads a file and counts the number of times a specified letter appears in the file as both uppercase and lowercase. The file name and the letter are passed as command line arguments.

The code has many practical use cases, specifically in data analytics. For instance, if you have a large text file and you want to count the frequency of a letter this code can be very helpful. As this code displays, you could use this code to count the number of times the letter "e" appears in a book. This can be useful for data processing and analysis as well as for debugging and troubleshooting purposes.

## Code + Explanation
```sh
import sys                                       
def letterfrequency(filename, letter):           
    with open(filename, 'r') as f:             
        text = f.read()                                                   
    upper_count = text.count(letter.upper())     
    lower_count = text.count(letter.lower())     
    return upper_count, lower_count              
filename = sys.argv[1]                             
letter = sys.argv[2]
upper_count, lower_count = letterfrequency(filename, letter)
print(f"The letter '{letter}' appears {upper_count} times as uppercase and {lower_count} times as lowercase in the file.")
```

- First I import sys to gain access to command line arguments. When the script is executed with above arguments(filename using argv[1]) and (letter as argv[2]), it will read the contents of the testing.txt1 file and count the number of occurrences of that letter and print the result to the console. Simply change the letter to any other to get the count of that specific letter. I struggled with this task for more than all the others but from researching this I was able to get it working, eventually. Upon receiving feedback on this task, I altered it to check for both uppercase and lowercase occurrences for the selected letter, which I will explain below. 

- To achieve the above - I imported the sys module as I found out that it was essential for command line arguments using argv as I will detail below. 

- I then defined my function letterfrequency and what I want from it aka the filename and the letter.

- Now the next few lines I got exclusively from my lecturer and the labs as I open the filename in read mode ('r') and assign it to the variable f. I used the with statement to ensure that the file is properly closed when the block is exited.

- Then I count the number of times a given letter appears in the input file - both in uppercase and lowercase, using upper_count and lower_count variables. I then convert the letters to uppercase using the upper() method and counts the number of times it appears using the count() method. The same method is repeated after converting the letter to lowercase using the lower() method. Finally. I return the count of uppercase and lowercase occurrences of the letter as a tuple. I initially tried to use a list rather than a tuple but I couldn't get it to work and I don't know why. Regardless, a tuple allows me to return multiple values from the function as a single object and it is signified by the comma between return upper_count, lower_count. 

- I then use the sys.argv arguments to allow me to do command line operations. First, I use the second command line argument (i.e. sys.argv[1]) to the variable filename. The second argument here is the texting.txt1 file. Unfortunately, I suffered hours upon hours of rather unenthusiastic head banging off the wall before I realised that the first argv (i.e. sys.argv(0)) is always the script's name itself aka in this instance; letterfrequency7.py rather than my text file.  Oh yes, that ruined many days indeed as I kept trying to open the script itself and not the text file and got nowhere fast. It was quite hilarious to be fair. Regardless, filename=sys.argv[1] assigns the second command line argument - the text file - to the variable filename.

- I then assigned the first character of the third command line argument (i.e. sys.argv[2]) to the variable letter - letter = sys.argv[2]. 
I didn't really know how to do much of this task and had to heavily rely on research and similar examples and explanations. From my understanding, filename is the second command line argument - done by using arg[1], which represents the filename of the text file to be read(testing.txt1). The letter is assigned the third element of the sys.argv list (sys.argv[2]) which then represents the letter whose frequency is to be counted. 

- Lastly, I call the letterfrequency function with the filename and letter variables as arguments and assign the returned values to upper_count and lower_count variables.

Then I use an f-string to print out a formatted string that includes the letter, upper_count, and lower_count variables. The printed string states how many times the specified letter appears as uppercase and lowercase in the file.

## Resources
1. [Stack over flow using count method](https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string) - used just to see ways of solving the problem (useless for command line arguments)

2. [Geeks used for educating myself on Count method](https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/) - More essential for me using the count method

3. [Stack over flow - command line arguments](https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments) - Showed me the import sys and how its used for command line arguments

4. [Geeks argv](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/) - This resource could have saved me countless idiotic hours of struggling. Found (eventually) that argv(0) was the script name and learned how to utilise them for command line arguments. 

5. [Python.org - ](https://docs.python.org/3/library/sys.html#sys.argv) - excellent reading on command line arguments

6. [Real strings - Strings](https://realpython.com/python-strings/) - learned to extract specific characters from a string in sys.argv[2][0] to extract the first character of the third command line argument. Very good resource.

7. [Code used for bones of code](https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/)

I used - https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ to get inspiration on how to do this task with regards how to use the in built count method that I used for both the upper and lower case counts. I then heavily relied on - https://www.youtube.com/watch?v=QJBVjBq4c7E to show me how to use command line arguments, specifically, what argv0, argv1, and argv2 represented and how to correctly type what I needed into the terminal aka: python .\letterfrequency7.py testing.txt1 e. The hardest part of this assignment was learning  how to properly use argv correctly, once I could somewhat do that without that much trouble, it wasn't that bad. Once I knew how to use the count method, I simply used it for both upper and lower case to get a more complete answer. 

So, overall this program calculates how many e's are in the testing.txt file by importing the sys module which allows for command line arguments (sys.argv). Once set up correctly as above - simply type:
```sh
python .\letterfrequency7.py testing.txt1 e
```
... and you will get the following response: The letter 'e' appears 0 times as uppercase and 24 times as lowercase in the file.

----

## plottask8.py <a name="plottask8.py"></a>

## Task
Create a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range [0, 10], 
on the one set of axes.

## Usage
To run, go to the appropriate repository or download the plottask8.py file and in the terminal, type:
```sh
python .\plottask8.py
```
A histogram will then be shown. 


## What is it and how can it be used
This code generates a histogram plot of a normal distribution with mean 5 and standard deviation 2 as well as a plot of the function h(x) = x^3.

This type of plot can be used to visualize the distribution of a dataset and can be helpful in identifying patterns or outliers in the data. It can also be used to compare the distribution of multiple datasets. Also, the plot of the function h(x) could be used to illustrate how the function behaves over a certain range of x values.

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

- This code generates a histogram of the above parameters as mentioned. To achieve this - I needed to import either seaborn or just use matplotlib alone. Both of these are Python visualization libraries that are widely used in the scientific and data analysis communities. I started off using matplotlib exclusively and got the code 'working'. However, I couldn't see the histogram no matter what I tried. I could see the plot, but no histogram. I left the computer for a while and tried importing seaborn as from what I gathered from research - it is a higher-level library built on top of Matplotlib that provides additional functionality and customization options for creating more 'aesthetically pleasing' visualizations. I went with this and realized later that the only reason my histogram was invisible earlier was because my 'bins' were set to 1 and my Alpha was set to 0. Both will result in no histogram as bins are simply the number of bars that are used to represent the data in a histogram. The bars represent a range of values in the data, and the height of each bar indicates the frequency or count of data points that fall within that range. By adjusting the number of bins - as I did from 1 to 10 - I went from seeing no histogram to seeing a completed histogram with the above plot. I also changed the alpha from 0 (which I later learned was transparent!) to 0.5 and voila - my histogram was finally viewable. This took a lot of trial and error and researching before I was happy with the end result. Seaborn - in the end - wasn't needed at all but my histogram looks slightly better with it so I left as is. 

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

7. [Main inspiration and education](https://www.datacamp.com/tutorial/histograms-matplotlib)

To complete this task, I relied heavily on - https://www.datacamp.com/tutorial/histograms-matplotlib a lot as it went into detail concerning the 'Introduction to Data Visualization with Seaborn'. It covered the basics of data visualization and demonstrated how to create various types of plots and graphs using Seaborn and Matplotlib. The course also included a section on histogram plots - which I found invaluable as it detailed bins, alpha labels and values and how to use them correctly. It also covered how to create and plot mathematical functions in Python which was also needed for this task. I also used - https://www.youtube.com/watch?v=tuDcsAxxOR8 - as this Youtube video went into huge detail about seaborn, its advantages and how to go about creating a histogram like what I created above. 

So, overall this program generates a histogram of the aforementioned requirements as soon as you type the following into the appropriate disrectory:

```sh
python .\plottask8.py
```
----

## License <a name="license"></a>
Unlicensed, free to use and distribute

## READMESources <a name="readmeSources"></a>
1. [Markdown Cheat sheet](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md) - Used to get all the necessary Markdown correct. Essential for headings, code snippets using ```sh, hyperlink external websites, table of content. 

2. [Markdown](https://www.markdownguide.org/getting-started) - Same as before

3. [README - all about how to write one](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/) - Important for knowing what to include like headings, table of contents and conclusion etc. 

## Bibliography <a name="bibliography"></a>
- Python Input() Function. Www.w3schools.com, www.w3schools.com/python/ref_func_input.asp.
- Python Int() Function. Www.w3schools.com, www.w3schools.com/python/ref_func_int.asp
- Python Arithmetic Operators.” Www.w3schools.com, www.w3schools.com/python/gloss_python_arithmetic_operators.asp.
- String — Common String Operations — Python 3.10.4 Documentation.” Docs.python.org, docs.python.org/3/library/string.html#format-specification-mini-language.
- Python String Format() Method.” Www.w3schools.com, www.w3schools.com/python/ref_string_format.asp.
- 1.4. Integer Arithmetic — Hands-on Python Tutorial for Python 3.” Anh.cs.luc.edu, anh.cs.luc.edu/handsonPythonTutorial/integer.html. Accessed 21 Apr. 2023
- Python String Concatenation.” GeeksforGeeks, 17 Dec. 2019, www.geeksforgeeks.org/python-string-concatenation
- String Slicing in Python.” GeeksforGeeks, 27 Dec. 2019, www.geeksforgeeks.org/string-slicing-in-python
- Perl - How to Mask Credit Card Number except the Last Four Digits Using Regex.” Stack Overflow, stackoverflow.com/questions/62304515. Accessed 01 Apr. 2023
- [Solved] Is There a Better Way to Mask a Credit Card Number in Python?” SolveForum, www.solveforum.com/forums/threads/solved-is-there-a-better-way-to-mask-a-credit-card-number-in-python.478573/. Accessed 25 Apr. 2023
-  Mask a Portion of a String Using RegExp.” Stack Overflow, stackoverflow.com/questions/43524845/mask-a-portion-of-a-string-using-regexp. Accessed 21 Mar. 2023
- Collatz Sequence. (Python 3).” Stack Overflow, stackoverflow.com/questions/33324432/collatz-sequence-python-3
- While Loop with If/Else Statement in Python.” Stack Overflow, stackoverflow.com/questions/36843103/while-loop-with-if-else-statement-in-python. Accessed 01 Mar. 2023
- Python If Statement.” Www.w3schools.com, www.w3schools.com/python/gloss_python_if_statement.as
- Python Lists.” W3schools.com, 2019, www.w3schools.com/python/python_lists.asp
- How to Find Current Day Is Weekday or Weekends in Python?” Stack Overflow, stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python. Accessed 16 Apr. 2023
- Python Dates.” Www.w3schools.com, www.w3schools.com/python/python_datetime.asp
- Import Module in Python.” GeeksforGeeks, 10 Nov. 2016, www.geeksforgeeks.org/import-module-python/
- Math - Python Square Function Using Newton’s Algorithm.” Stack Overflow, stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm. Accessed 18 Apr. 2023
- Babylonian Method for Square Root.” GeeksforGeeks, 20 Dec. 2009, www.geeksforgeeks.org/square-root-of-a-perfect-square
- Python, Real. “Python “While” Loops (Indefinite Iteration) – Real Python.” Realpython.com, realpython.com/python-while-loop
- Python Math Function | Sqrt().” GeeksforGeeks, 11 Jan. 2018, www.geeksforgeeks.org/python-math-function-sqrt. Accessed 25 Apr. 2023
- Python, Real. “How to Find an Absolute Value in Python – Real Python.” Realpython.com, realpython.com/python-absolute-value. Accessed 25 Apr. 2023
- Tolerance Documentation Release Alisue. 2017
- Python - Count the Number of Occurrences of a Character in a String.” Stack Overflow, stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
- Python | Count Occurrences of a Character in String.” GeeksforGeeks, 22 Nov. 2018, www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string. Accessed 25 Apr. 2023.
- Python - How Do I Access Command Line Arguments?” Stack Overflow, stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments. Accessed 10 Apr. 2023
- Sys — System-Specific Parameters and Functions.” Python Documentation, docs.python.org/3/library/sys.html#sys.argv. Accessed 01 Apr. 202
- Python, Real. “Strings and Character Data in Python – Real Python.” Realpython.com, realpython.com/python-strings. Accessed 25 Apr. 2023
- Count the Number of Times a Letter Appears in a Text File in Python.” GeeksforGeeks, 24 Nov. 2020, www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python. Accessed 25 Apr. 2023
- Jovian. “Visualization with Matplotlib and Seaborn | Data Analysis with Python (5/6) | Free Certification.” YouTube, 30 Dec. 2020, www.youtube.com/watch?v=tuDcsAxxOR8. Accessed 25 Mar. 2023
- User Guide and Tutorial — Seaborn 0.11.2 Documentation.” Seaborn.pydata.org, seaborn.pydata.org/tutorial.htm
- Users Guide — Matplotlib 3.5.0 Documentation.” Matplotlib.org, matplotlib.org/stable/users/index.html.
- Seaborn Tutorial 2021.” Www.youtube.com, www.youtube.com/watch?v=6GUZXDef2U0
- Seaborn.histplot — Seaborn 0.11.2 Documentation.” Seaborn.pydata.org, seaborn.pydata.org/generated/seaborn.histplot.html
- “Pyplot Tutorial — Matplotlib 3.5.1 Documentation.” Matplotlib.org, matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
- Histograms in Matplotlib.” Www.datacamp.com, www.datacamp.com/tutorial/histograms-matplotlib
- Chapellier, Cyril. “Markdown Cheatsheet.” GitHub, 25 Apr. 2023, github.com/tchapi/markdown-cheatsheet/blob/master/README.md. Accessed 25 Apr. 2023
- Getting Started | Markdown Guide.” Www.markdownguide.org, www.markdownguide.org/getting-started. Accessed 25 Apr. 2023
- Nyakundi, Hillary. “How to Write a Good README File for Your GitHub Project.” FreeCodeCamp.org, 8 Dec. 2021, www.freecodecamp.org/news/how-to-write-a-good-readme-file



## Conclusion <a name="conclusion"></a>
Firstly, I want to thank the very fortunate souls that have reached this far in and have had the great 'privilege' of reading my rather lengthy readme. I took a lot from  these tasks. To any programmer worth any salt at all, I'm sure the above tasks are mere child's play - if even that. For me, however - I struggled immensely, struggled sensationally and then to change things up - struggled some more. I panicked when i couldn't get my collatz to collatz right away; when I didn't understand how to make dynamic strings when masking CC numbers; when I had no idea what a command line argument was, never mind implement two. However, I also got a great sense of satisfaction when i - in the end - could resolve those problems through exhaustive research, discussions with my fellow classmates and examples of similar code implementations online. I am still a beginner - perhaps even that is too esteemed a term. What the above tasks have done for me is introduce me to the world of scripting and python. I've grown a fair bit from being intimidated as to how to print Hello world! to where I am now. So, I may be very low on the development ladder - but the weekly pands-problem-sheet assignments have helped me improve and learn to think logically.  
