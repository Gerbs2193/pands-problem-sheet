#: Author Gerard Ball
#: plottask8.py
#: A program that displays a Histogram of a normal distribution of 1k values with mean of 5 and a standard deviation of 2 and a plot of the function h(x)=xcubed in the range [0,10] on the one set of axes.


import numpy as np                                          #numpy library imported for random values, seaborn for histogram (tried plt.hist first but for some reason kept getting errors) and matplotlib for plotting
import seaborn as sns
import matplotlib.pyplot as plt
values = np.random.normal(5, 2, 1000)                       #1000 random random values from noraml distribution with mean of 5 and standard deviation of 2. Stores them in values variable
x = np.linspace(0, 10, 100)                                 #generates an array of 100 values between 0 and 10 and stores them in the x variable
y=x**3                                                      #calculates the function and stores it in y variable
sns.histplot(values, bins=10, alpha=0.5, label="Histogram") #generates histogram using seaborns histplot. bins is used for height of the values (used 50 originally, had to go to 10 as 50 was far too small). 
                                                            #alpha = 0.5 effects the bar transparency. 0 is transparent so invisible and 0.5 viewable. Took too long to realise where my invisible histogram got to. 
                                                            #label sets the label in the legend
plt.plot(x, y, color = "red", label="h(x)=x^3")             #plots the function by using matplotlibs plot function. label for function in legend
plt.title("Week08plottask.py - Histogram of funtion h(x)=x^3") #set title, x and y axis label and legend for plot
plt.xlabel("Value")
plt.ylabel("Frequency or h(x)")
plt.legend()
plt.show()                                                 #I display the plot
