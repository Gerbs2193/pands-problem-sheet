#: Author Gerard Ball
#: Week08plottask.py
#: A program that displays a Histogram of a normal distribution of 1k values with mean of 5 and a standard deviation of 2 and a plot of the function h(x)=xcubed in the range [0,10] on the one set of axes

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


values = np.random.normal(5, 2, 1000)

x = np.linspace(0, 10, 100)

y=x**3

sns.histplot(values, bins=10, kde=False, alpha=0.5, label="Histogram")
plt.plot(x, y, color = "red", label="h(x)=x^3")

plt.title("Histogram of funtion h(x)=x^3")
plt.xlabel("Value")
plt.ylabel("Frequency or h(x)")
plt.legend()

plt.show()