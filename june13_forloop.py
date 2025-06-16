
import math
import numpy as np
#creating a new list and adding items into it

#we can start a variable with an empty list
ages = []
#
# #let us add the age 56 into this list:
ages.append(56)
ages.append(16)
print(ages)
#
# #insert an item at any location
ages.insert(1, 85)
print(ages)
#
ages.insert(2,11)
print(ages)

#exercise: write a function that returns a list of ages which are smaller than a given limit.
ages = [34, 25, 15, 76, 68, 50, 23]
def young_people(ages, limit):
    y = []
    for age in ages:
        if age <= limit:
            y.append(age)
    return y

Y = young_people(ages, 40)
print(Y)

y_30 = young_people(ages, 30)
print(y_30)

y_10 = young_people(ages, 10)
print(y_10)

#tuples are also useful containers like lists, but we create them using parentheses instead of
#square brackets. they cannot be changed/appended to like lists
#
ages1 = (34,25,15,76,68,50,23)
# ages1.append(45) would throw an error
#
# #we can edit lists
ages[2] = 35 #replace the number in that index
print(ages)
#
print('---------')
# #using a while loop to visit each item in a list needs redundant code. For loops are more concise
for age in ages:
    print(age)
#
# #tuple unpacking
person1  = ('Luna', 25)
person2 = ('Maria', 37)
name, age = person1
print(name, age)

#exercise: go through the list of ages and print only ages between 20 and 55
ages = [34,25,15,76,68,50,23]
for age in ages:
   if 20 < age < 55:
     print(age)

#exercise: find the average age
def average(x):
    tot = 0
    for age in ages:
        tot += age
    average = tot/len(ages)
    return average

#exercise: write a function to calculate standard deviation
def variance(x):
    xbar = average(x) #first find the mean of x aka xbar
    s_sum = 0
    for a in x:
        s_sum += (a - xbar) ** 2 #here find the total of (x1 - xbar) ** 2 + (x2 - xbar) ** 2 + ....
    var = s_sum/len(x) #divide the total by n
    return var

print(variance(ages))

ages = np.array([34,25,15,76,68,50,23])
print(f'variance: {ages.var()}') #check above result with numpy
print(f'standard deviation: {ages.std()}')

#exercise: counting zero crossing
#write a function that finds the number of times a signal crosses the axis

s = [3,5,-2,-7,1,-2,-3,-5,9,5,-1,1]
def num_zero_crossing(s):
    c = 0
    k = 1
    while k < len(s):
        if s[k-1] * s[k] < 0:
            c += 1
        k += 1
    return c

cs = num_zero_crossing(s)
print(cs) #6 is printed

# These are the average zero-crossings for a family of four
f = [100, 200, 125, 230]

#our security system opens the door if a test person's zero crossing is within +-10 of any family member's crossing
def open_or_not(f, t):
    """
    :param f: a list of zero crossings for a family
    :param t: a zero crossing of a test person
    :return: True when T is within +-10 units of any member in 'f'
    """
    for z in f:
        delta = abs(z - t)
        if delta < 10:
            return True
    return False

print(open_or_not(f, 108))

#exercise: write a function that finds the closest number in a list to a given test number T
# for instance, if the list is F = [100,200,125,230] and the test number is T = 220,
# the item 230 is closest to T.
def closest_number(f, t):
    """
    :param f: a list of numbers
    :param t: the test number
    :return: the closest number from the list of numbers to the test number
    """
    vals  = []
    for a in f:
        vals.append(abs(a-t))
    cl = min(vals)
    min_index = vals.index(cl)
    return f[min_index]

print(closest_number(f, 215))
