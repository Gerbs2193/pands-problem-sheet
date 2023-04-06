#: Author Gerard Ball
#: Week08plottask.py
#: A program that displays a Histogram of a normal distribution of 1k values with mean of 5 and a standard deviation of 2 and a plot of the function h(x)=xcubed in the range [0,10] on the one set of axes

#numpy library imported for random values, seaborn for histogram (tried plt.hist first but for some reason kept getting errors) and matplotlib for plotting
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#1000 random random values from noraml distribution with mean of 5 and standard deviation of 2. Stores them in values variable
values = np.random.normal(5, 2, 1000)

#generates an array of 100 values between 0 and 10 and stores them in the x variable
x = np.linspace(0, 10, 100)

#calculates the function and stores thrm in y variable
y=x**3

#generates histogram using seaborns histplot. bins is used for height of the values (used 50 origi9nally, had to go to 10 as 50 was far too small). 
#alpha = 0.5 effects the bar transparency. 0 is transparent so invisible and 0.5 viewable. Took too long to realise where my invisible histogram got to. 
#label sets the lebel in the legend
sns.histplot(values, bins=10, alpha=0.5, label="Histogram")

#plots the function by using matplotlibs plot function. label for function in legend
plt.plot(x, y, color = "red", label="h(x)=x^3")

#set title, x and y axis label and legend for plot
plt.title("Week08plottask.py - Histogram of funtion h(x)=x^3")
plt.xlabel("Value")
plt.ylabel("Frequency or h(x)")
plt.legend()

#we disp;lay the plot
plt.show()

