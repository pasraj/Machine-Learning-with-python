import numpy as np
from scipy import stats


speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Mean :- The Average value
x = np.mean(speed)

#Median :- The Median value is the value in the middle after the sorted all value
#Note :- if there are two number in the middle divide the sum of those numbers by two
y = np.median(speed)


#Mode :-  The Mode value is the value that appears the most of times
z = stats.mode(speed)


print("average speed is :", format(x, '.2f'))
print("median of the speed is : ", y)
print("mode :", z)
