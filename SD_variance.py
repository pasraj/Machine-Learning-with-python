import numpy as np

data = [5, 10, 25, 30, 50]

# Standard Deviation :- Standard Deviation is a number that describes how  spread out the values are.

sd = np.std(data)
print("Standard Deviation : ", format(sd, '.3f'))

# Variance :- Variance is the another number that indicates how spread out the values are.
varinace = np.var(data)

print("Variance : ", varinace)


# Square root of the variance is Standard deviation
num = np.sqrt(varinace)

print("Square root of Variance ( Standard Variance ) : ", format(num, '.3f'))