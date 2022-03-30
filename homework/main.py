# Jesus Minjares
# Master of Science in Computer Engineering

from asyncio.subprocess import SubprocessStreamProtocol
from functions import *

data = np.array([   13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25,30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70 ])

print("Part A")
print("-"*15)
print("Mean: ", mean(data), " Median: ", median(data))

print("Part B")
print("-"*15)
print("Mode: ", mode(data))


print("Part C")
print("-"*15)
print("Midrange: ", midrange(data))

print("Part E")
print("-"*15)
print("Five Number Summary")
five_num = five_number_summmary(data)
print("Min: ", five_num['min'])
print("Q1: ", five_num['q1'])
print("Median: ", five_num['median'])
print("Q3: ", five_num['q3'])
print("Max: ", five_num['max'])



# x = np.array([22,1,42,10])
# y = np.array([20, 0, 36, 8])


x = np.array([1,2])
y = np.array([3,5])

# using custom functions
print(euclidean(x,y))
print(manhattan(x,y))
print(minkowski(x,y,3))
print(supremum_distance(x,y))

# using lnorm
print(lnorm(x,y,2))
print(lnorm(x,y,1))
print(lnorm(x,y,3))
print(supremum_distance(x,y))