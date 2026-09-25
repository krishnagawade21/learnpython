import numpy as np
import matplotlib.pyplot as plt

#Triangular membership function
def triangular(x, a, b, c):
    return np.maximum(np.minimum((x-a)/(b-a), (c-x)/(c-b)),0)

#Input marks
x = np.arange(0, 101, 10)

#Fuzzy membership functions
low = triangular(x, 0, 25, 50)
medium = triangular(x, 25, 50, 75)
high = triangular(x, 50, 75, 100)

#Display membership function
print("Marks\tLow\tMedium\tHigh")

for i in range (len(x)):
    print (x[i], "\t", round(low[i], 2),
           "\t", round(medium[i], 2),
           "\t", round(high[i], 2))

#ANN input
X = np.column_stack((low, medium, high))

print("\nANN Input:")
print(X)

#plot
plt.plot(x, low, label="LOw")
plt.plot(x, medium, label="Medium")
plt.plot(x, high, label="High")
plt.grid()
plt.show()
