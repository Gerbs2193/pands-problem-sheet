# pands-problem-sheet
# Problems 2023

This repository is all about the weekly problem set issued by Andrew during the Programming and Scripting module in the Higher Diploma in Data Analytics course in ATU.\

Here, i will go through and explain how i solved each weekly problem sheet task, the resources i used that were essential to both my understanding of the problem being asked and how i implemented the solutions using said resources. I had next to zero experience using any programming language and, as such, i relied heavily on the extra reading Andrew supplied through the module page and the almost limitless resources online. 

## Table Of Contents
*[weekly tasks](#weekly-tasks)
*[helloworld.py](#helloworld.py)
*[bank.py](#bank.py)
*[accounts.py](#accounts.py)
*[collatz.py](#collatz.py)
*[weekday.py](#weekday.py)
*[squareroot.py](#squareroot.py)
*[leterfrequency.py](#letterfrequency.py)
*[plottask.py](#plottask.py)

### Weekly tasks
======
#### helloworld.py

##### Task

Write a program that displays Hello World! when  its run. This is a simple program that prints "Hello World!" to the sonsole within the 'Week01helloworld.py'file contained in the Pands-Problem-Sheet directory

##### Usage
To run, navigate to the 'helloworld.py' file and enter the following command in the terminal:
```sh
python .\helloworld.py
```
##### code
print("Hello World!)

##### Output
Program prints Hello World!

##### Resources and Struggles
No resources needed other than following Andrew's lead during the lab. However, i hilaroiusly kept getting an error in the terminal as i didnt know the command in the terminal had to be the name of the file, rather than the output of Hello World! I kept typing python .\Hello World!.py rather than python .\helloworld.py. Embarrassing to look back on indeed.

----


#### bank.py

##### Task

Write a program  that promts the user to read in two money amounts in cents. Add them and print the result in euro form

##### Usage
To run, navigate to the 'bank.py' file and enter the following command in the terminal:
```sh
python .\bank.py. 
Input 2 separate amounts in cents when instructed and await the result
```
##### Code + Explanation
```sh
amount1 = int(input("Please enter first amount in cents"))
amount2 = int(input("Please enter second amount in cents))
answer = (amount1 + amount2)/100
print(f"The sum: €{answer}")
```

- The first line prompts the user to enter the first amount in cents using the input() function. I used int(input) as i needed to  convert the user's input (A string) into an integer, which is then assigned to the amount1 variable. If i had just used input() and tried to add both variables amounts together using this method id get an error as i cant perform a mathematical operation between a string and an integer. int(input) solves this by converting the user's input to an integer and allowoing for arithmetic calculations. amount1 is the variable

- The second line same logic as first.

- Third line adds the two variable amounts together and divides the result by 100 to get the accurate decimal euro total. Then the result of the calculation is assigned to the answer variable.

- Final line I used f-string to print the value of answer in the format "€{answer}". At the point in time of doing this task, i dodnt know why f-string wa sused and initially used: print("The sum: €" + str(answer)) as that is what i found people doing on Stackoverflow for various problems. Alas,I've been hearing using an f-string is considered more readable and convenient, as it allows you to easily include variables and expressions in your strings. I still find myself inconsisteent with how i code. 

##### Output
Program prints amount in euro decimal depoending on user input. Example, user inputs 90 and 50 the output would be 
€1.4

##### resources

1. [Python Input() Function](https://www.w3schools.com/python/ref_func_input.asp)
2. [Python int() Function](https://www.w3schools.com/python/ref_func_int.asp)
3. [Python Division Operator](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp)
4. [Python f-Strings](https://realpython.com/python-f-strings/)

I used all the above resources, specifically the w3schools int()function to do this task. I also used Stackoverflow just to see examples of people using f-strings. 

So overall, this program prompts the user to enter two amounts in cents, adds them together, converts the result to euros, and prints the result in the format "€{answer}".

----

#### accounts.py

##### Task

Write a program that reads in a 10 character account number and outputs the account number with only the last 4 digits showing. Replace first 6 with.

##### Usage

To run, nativage to 'accounts.py' file and enter the following command in the terminal:
```sh
 python .\accounts.py
 ```
 ##### Code + Explanation
 ```sh
credit_card_number = input("Enter your credit card number: ")
masked_cc_number = " xxx xxx " + credit_card_number[-4:]
print("Masked credit card number:", masked_cc_number)
```

- First line of code requests the user's credit card number as  inpuy and stores it as a string in the variable I called credit_card_number.

- Second line of code took many revisions over many weeks but eventually, from research online, combined concatenating (what i understand to be combining 2 or more strings together into 1 string) and slicing all but the last 4 digits using [-4:]. The "xxx xxx" is a string that will mask the first 6 digits of a 10 digit number. The [-4:] part of the credit_card_number string refers to a slice of the string that starts at the fourth last character and continues to the end of the string. This slice extracts the last four digits of the credit card number and concatenates it with the masked string to produce the masked credit card number. Also, you can input any length of number you wish - doesnt have to be 10 digits - and you will always get the masking of the final 4 digits. However, with this current method, the masking string only masks 6 digits. I initially had "xxxx xxxx xxxx" to simulate the ususal length of a standard CC. From the bunker deep rabbit hole i went down researching the above solutions, i found i could also dynamically use the masking string x to cover every user inputted digit minus the last 4. I didnt 100 percent understand all of it at that time so i just stuck with the above which i did. 

- Third line In my code we simply print out the final masked CC number. We have a string called "Masked credit card number:" and a variable called masked_cc_number that has the masked credit card number. We then print the two as a single, displaying our desired masked CC number

##### Output
Program masks CC number. "Enter your credut card number" - example = 012 347 1234
Masked credit card number:  xxx xxx 1234

##### Resources
1. [Python String Concatenation](https://www.geeksforgeeks.org/python-string-concatenation/)
2. [Python Slice Notation - GeeksforGeeks](https://www.geeksforgeeks.org/string-slicing-in-python/)
3. [masking last 4 digits of CC](https://stackoverflow.com/questions/62304515/how-to-mask-credit-card-number-except-the-last-four-digits-using-regex)

I used all above resources tirelessly. Initially, i onlu used stackoverflow and simply found an example of code from someone else and went with that. However, that only worked if the string was known like 1234567891 and then xxxxxx7891 would be the output. Not dynamic. Changed when I learned to concatenate the stings. 

So, overall, this code - using concatenation, masking and slicing - disguises the first 6 digits of a given input and onlu reveals the last 4

----

#### collatz.py

##### Task

Write a program that asks the user to input anh positive integer and outputs the successive values of the following calculation. At each step calculate the next value and, if it is even, divide it by 2, but if it is odd, multiply it by 3 and add 1. End program if current value is 1.

##### Usage

To run, go to the python terminal and type:
```sh
python .\collatz.py and enter a positive integer as intructed. 
```

##### Code + Explanation
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

- First few lines we use a non-print function for the first time called collatz with num being what we want it to do. sequence = [] was added many weeks after initial github push as i eventually noticed Andrew's collatz displayed as a list whereas mine - initially - did not. This line creates an empty list called sequence which will be used to store the Collatz sequence later. This code was also my first introduction in practice to while loops and if statements. 

- The next is the formula for calculating the collatz using python. I simply looked online for the formula and how to implement it properly. The sequence.append(num) line adds the current value of num to the end of the sequence list after doing the collatz to it. So to my understanding, each time the loop runs, it adds the current value of num to the list before moving on to the next iteration. It ends when we get to 1 as the project instructs us to do. We get the (final) sequence returned then. 

- However, the next part wasn't essentail im sure - it was more a consequence of my love affair with rabbit holes. I wanted to issue a warning for the user if they entered a negative number. To do this, i simply introduced a while lopp whereby if the num was less than 0 (<0) aka NOT a positive integer, the console would print "Detected negative integer number. Please enter a positive integer number". Then, my code prompts the user to input a positive integer number with the line num = int(input("Enter a positive integer number: ")), and assigns the new input value to num. Finished

##### Output

Program performs collatz. Example - "Enter a positive integer number:"   10
[10, 5, 16, 8, 4, 2, 1]

##### Resources

1. [Collatz - Stack Over Flow](https://stackoverflow.com/questions/33324432/collatz-sequence-python-3) - used this for collatz formula though my implementation uses a list and corrects user for wrong inputs as well as different coding preferences

2. [While loops - Stack Over Flow](https://stackoverflow.com/questions/36843103/while-loop-with-if-else-statement-in-python) - Used this to see many practical implementations of while loops. 

3. [W3Schools - If Statements](https://www.w3schools.com/python/gloss_python_if_statement.asp) - Used Andrew's lecturs and labs but also this resource when educating myself on if statements.

4. [W3Schools - Lists](https://www.w3schools.com/python/python_lists.asp) - Went back over lists again when i realised my initial problem didnt output the sequence in a list. This link showed me how to do it. 

So, overall this code performs the collatz using the above found formula, outputs the colatz sequence.append(num) into the new list. Used while loops and if statement to complete the collatz formula. Added safeguards in the event of a user inputing a negative integer number using another while loop. 

----

#### weekday.py

##### Task

Write a program that outputs whether or not today is a weekday. 

##### Usage

To run, go to the appropriate repository or download the weekday.py file and in the terminal, type:
sh```
python .\weekday.py ``` Subsequent to this, you will be told whether it is the weekend ("Weekend, yessssss!") or a weekday (Yes, today is a Weekday - how positively wonderful..."). This is done using importing, which i will explain upon below. 

##### Code + Explanation

```sh
import datetime
weekno = datetime.datetime.today().weekday()
if weekno < 5:
print ("Yes, today is a Weekday - how positively wonderful...")
else: 
 print ("Weekend, yessssss!") 
```

This program introduced me to importing and modules. They were integral (for me) to get this program to work as instructed. So, we start by importing the datetime module. I did this after researching online and seeing that the aforementioned module is needed to give us access to the current date and time and allows us to perform operations with it. 

The second line of code i got directly off of Stackoverflow as once i imported the datetime, i didnt know where to go from there at first. In this line, I creayed a variable called weekno. We get the current date and time using the datetime.today() function which then calls the weekday() method to get the day of the week as an integer between 0 (Monday) and 6 (Sunday). The resulting integer is assigned to the variable weekno. The datetime module calls 0 monday and 6 Sunday - and everything in between as you'd expect. So this was an essential module in determining the day of the week in python. 

We then use an if statement to determine if its a weekday and two print functions. as mentioned above, 0 represents Monday using the imported datetime module and 6 represents Sunday. So, we use the if statement to determine that the variable weekno <5: (less than 5) - then we have determined that the day is a weekday as the current day is below 5. However, if it is greater than 5 then we have determined it is a weekend as the current number is greater than 5. I print out two opposing print functions that tell the user whether they're perusing the terminal on a weekday(yay), or not (oh no).

##### Output

Determines whether it is weekday, or weekend
```sh
python .\weekday.py
if <5: "(Yes, today is a Weekday - how positively wonderful...")
else: "("Weekend, yessssss!")
```

#### Resources

1. [Stack over flow code used](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python)
 
2. [w3schools datetime](https://www.w3schools.com/python/python_datetime.asp)

3. [Python importing](https://www.geeksforgeeks.org/import-module-python/)

So, overall this code determines whether it is a weekday or weekend by importing the datetime module in python. 

----

#### squareroot.py

##### Task

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
Use Newton's appromimation formula to do this. (Ended up using similiar Babylonian method)

##### Usage

To run, go to the appropriate repository or download the squareroot.py file and in the terminal, type:
```sh
python .\squareroot.py 
``` 
subsequent to this, you will be prompted to 'Enter number" then you will be told the "Approximate Square root of number" of what you inputed. 

##### Code + Explanation

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
I start here by defining a function called my_sqrt and we want it to produce the argument (n). my_sqrt was used as the function that approximates the square root of a given number using the Babylonian method. The basic formula is this: Root = 0.5 *(x +(N/x)) where x is any guess which can be assumed to be N or 1. I found online examples of this formula being used in practice and took heavy inspiration from it, specifically, one on Stackoverflow. However, as you'll soon see, my code iterates a lot more until the approximation is very accurate. 

Then I create a variable called approx and equal it to half of the input number n aka n/2.

I then create a variable called closer. The value of closer is calculated using the average of the current approximation approx and n/approx, which is a better approximation of the square root of n. This new value I  then assign to the closer variable.

I then introduce a while loop. In here, the loop repeats until the current approximation closer is sufficiently close to the previous approximation approx. The != operator tests if closer and approx are not equal.

I then update the approximations of the square root of n by setting approx to the current approximation closer and then computing a better approximation of the square root of n by taking the average of approx and n/approx. I keep iterating this until satisfied. The reason for repeating these two lines multiple times is to increase the accuracy of the approximation of the square root of n. Initially, i did this once and got the approximation square root of 81 to be 45. However, uponn iterating the code several more times in the while loop, i eventually got 9.00etc as the square root of 81. 

I returned the finished approximation and the while loop has stopped iterating. 

I then simply code the input and print my_sqrt(n)).

##### Resources

1. [Stack over flow code example](https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm) - code realised from this example. Mine just iterates many more times for added accuraccy. 

2. [Babylonian](https://www.geeksforgeeks.org/square-root-of-a-perfect-square/)

3. [iterating](https://realpython.com/python-while-loop/)

4 . [my_sqrt](https://www.geeksforgeeks.org/python-math-function-sqrt/)

So, overall this program calculates an approximation of the user input using the babylonian method and uses a function my_sqrt and while loops and iteration to achieve a relatively very accurate result. 

----





 






