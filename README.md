# pands-problem-sheet
# Problems 2023

This repository is all about the weekly problem set issued by Andrew during the Programming and Scripting module in the Higher Diploma in Data Analytics course in ATU.\

Here, i will go through and explain how i solved each weekly problem sheet task, the resources i used that were essential to both my understanding of the problem being asked and how i implemented the solutions using said resources. I had next to zero experience using any programming language and, as such, i relied heavily on the extra reading Andrew supplied through the module page and the almost limitless resources online. 

## Table Of Contents
*[weekly tasks](#weekly-tasks)
*[week01helloworld.py](#week01helloworld.py)
*[week02bank.py](#week02bank.py)
*[week03accounts.py](#week03accounts.py)
*[week04collatz.py](#week04collatz.py)
*[week05weekday.py](#week05weekday.py)
*[week06squareroot.py](#week06squareroot.py)
*[week07leterfrequency.py](#week07letterfrequency.py)
*[week08plottask.py](#week08plottask.py)

### Weekly tasks
======
#### week01helloworld.py

##### Task

Write a program that displays Hello World! when  its run. This is a simple program that prints "Hello World!" to the sonsole within the 'Week01helloworld.py'file contained in the Pands-Problem-Sheet directory

##### Usage
To run, navigate to the 'Week01helloworld.py' file and enter the following command in the terminal:
```sh
python .\week01helloworld.py
```
##### code
print("Hello World!)

##### Output
 Hello World!

##### Resources and Struggles
No resources needed other than following Andrew's lead during the lab. However, i hilaroiusly kept getting an error in the terminal as i didnt know the command in the terminal had to be the name of the file, rather than the output of Hello World! I kept typing python .\Hello World!.py rather than python .\week01helloworld.py. Embarrassing to look back on indeed.

----


#### week02bank.py

##### Task

Write a program  that promts the user to read in two money amounts in cents. Add them and print the result in euro form

##### Usage
To run, navigate to the 'Week02bank.py' file and enter the following command in the terminal:
```sh
python .\week02bank.py. 
Input 2 separate amounts in cents when instructed and await the result
```
##### Code + explanation
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
prints amount in euro decimal depoending on user input. Example, user inputs 90 and 50 the output would be 
€1.4

##### resources

1. [Python Input() Function](https://www.w3schools.com/python/ref_func_input.asp)
2. [Python int() Function](https://www.w3schools.com/python/ref_func_int.asp)
3. [Python Division Operator](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp)
4. [Python f-Strings](https://realpython.com/python-f-strings/)

I used all the above resources, specifically the w3schools int()function to do this task. I also used Stackoverflow just to see examples of people using f-strings. 

So overall, this program prompts the user to enter two amounts in cents, adds them together, converts the result to euros, and prints the result in the format "€{answer}".

----

#### week03accounts.py

##### Task

Write a program that reads in a 10 character account number and outputs the account number with only the last 4 digits showing. Replace first 6 with.

##### Usage

To run, nativage to 'week03accounts.py' file and enter the following command in the terminal:
```sh
 python .\week03accounts.py
 ```
 ##### Code + explanation
 ```sh
credit_card_number = input("Enter your credit card number: ")
masked_cc_number = " xxx xxx " + credit_card_number[-4:]
print("Masked credit card number:", masked_cc_number)
```

- First line of code requests the user's credit card number as  inpuy and stores it as a string in the variable I called credit_card_number.

- Second line of code took many revisions over many weeks but eventually, from research online, combined concatenating (what i understand to be combining 2 or more strings together into 1 string) and slicing all but the last 4 digits using [-4:]. The "xxx xxx" is a string that will mask the first 6 digits of a 10 digit number. The [-4:] part of the credit_card_number string refers to a slice of the string that starts at the fourth last character and continues to the end of the string. This slice extracts the last four digits of the credit card number and concatenates it with the masked string to produce the masked credit card number. Also, you can input any length of number you wish - doesnt have to be 10 digits - and you will always get the masking of the final 4 digits. However, with this current method, the masking string only masks 6 digits. I initially had "xxxx xxxx xxxx" to simulate the ususal length of a standard CC. From the bunker deep rabbit hole i went down researching the above solutions, i found i could also dynamically use the masking string x to cover every user inputted digit minus the last 4. I didnt 100 percent understand all of it at that time so i just stuck with the above which i did. 

- Third line In my code we simply print out the final masked CC number. We have a string called "Masked credit card number:" and a variable called masked_cc_number that has the masked credit card number. We then print the two as a single, displaying our desired masked CC number

##### Output
Masks CC number. "Enter your credut card number" - example = 012 347 1234
Masked credit card number:  xxx xxx 1234

##### Resources
1. [Python String Concatenation](https://www.geeksforgeeks.org/python-string-concatenation/)
2. [Python Slice Notation - GeeksforGeeks](https://www.geeksforgeeks.org/string-slicing-in-python/)
3. [masking last 4 digits of CC](https://stackoverflow.com/questions/62304515/how-to-mask-credit-card-number-except-the-last-four-digits-using-regex)

I used all above resources tirelessly. Initially, i onlu used stackoverflow and simply found an example of code from someone else and went with that. However, that only worked if the string was known like 1234567891 and then xxxxxx7891 would be the output. Not dynamic. Changed when I learned to concatenate the stings. 

So, overall, this code - using concatenation, masking and slicing - disguises the first 6 digits of a given input and onlu reveals the last 4

----

#### week04collatz

##### Task

Write a program that asks the user to input anh positive integer and outputs the successive values of the following calculation. At each step calculate the next value and, if it is even, divide it by 2, but if it is odd, multiply it by 3 and add 1. End program if current value is 1.

##### Usage

To run, go to the python terminal and type:
```sh
python .\week04collatz.py and enter a positive integer as intructed. 
```

##### Code + explanation
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

First few lines we use a function for the first time called collatz with num being what we want it to do. sequence = [] was added many weeks after initial github push as i eventually noticed Andrew's collatz displayed as a list whereas mine - initially - did not. This line creates an empty list called sequence which will be used to store the Collatz sequence later. This code was also my first introduction in practice to while loops and if statements. The next is the formula for calculating the collatz using python. I simply looked online for the formula and how to implement it properly. The sequence.append(num) line adds the current value of num to the end of the sequence list after doing the collatz to it. So to my understanding, each time the loop runs, it adds the current value of num to the list before moving on to the next iteration. It ends when we get to 1 as the project instructs us to do. We get the (final) sequence returned then. However, the next part wasn't essentail im sure - it was more a consequence of my love affair with rabbit holes. I wanted to issue a warning for the user if they entered a negative number. To do this, i simply introduced a while lopp whereby if the num was less than 0 (<0) aka NOT a positive integer, the console would print "Detected negative integer number. Please enter a positive integer number". Then, my code prompts the user to input a positive integer number with the line num = int(input("Enter a positive integer number: ")), and assigns the new input value to num. Finished

##### Output

Performs collatz. Example - "Enter a positive integer number:"   10
[10, 5, 16, 8, 4, 2, 1]

##### Resources

1. [Collatz - Stack Over Flow](https://stackoverflow.com/questions/33324432/collatz-sequence-python-3) - used this for collatz formula though my implementation uses a list and corrects user for wrong inputs as well as different coding preferences

2. [While loops - Stack Over Flow](https://stackoverflow.com/questions/36843103/while-loop-with-if-else-statement-in-python) - Used this to see many practical implementations of while loops. 

3. [W3Schools - If Statements](https://www.w3schools.com/python/gloss_python_if_statement.asp) - Used Andrew's lecturs and labs but also this resource when educating myself on if statements.

4. [W3Schools - Lists](https://www.w3schools.com/python/python_lists.asp) - Went back over lists again when i realised my initial problem didnt output the sequence in a list. This link showed me how to do it. 

So, overall thus code performs the collatz using the above found formula, outputs the colatz sequence.append(num) into the new list. Used while and if statement to complete the collatz formula. Added safeguards in the event of a user inputing a negative integer numbe using another while loop. 

----

#### week05weekday





