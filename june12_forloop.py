k = 1
while k<= 10:
    if k == 4:
        continue
    print(k)
    k += 1

# if we want to skip printing 4 in the above program, we can use the 'continue' statement.
# python skips all lines following the continue line, and continues onto the next cycle.

k = 0
while k < 10:
    k += 1
    if k == 4:
        continue
    print(k)

#exercise: print even numbers from 1 to 100
k = 0
while k < 100:
    k += 1
    if k % 2 != 0:
        continue
    print(k)

#exercise: print odd numbers from 1 to 100
k = 0
while k < 100:
    k += 1
    if k % 2 == 0:
        continue
    print(k)

#break statement
# # python breaks the loop and goes to the next statement when it reaches this
i = 1
while i <= 1000000:
    if i > 15:
        break
    i += 1
    print(i)
#
# exercise: 4,7,10,...301 except between 20 and 280
k = 4
print(k)
while k <= 301:
    k += 3
    if 20 <= k <= 280:
        continue
    if k > 301:
        break
    print(k)

# cost minimization
# f(p) = 2 * (p-3)^2 + 15
# its derivative is f'(p) = 4(p-3)

#set the parameters
alpha = 0.01
#start with a random guess for the price
p = 2
#find the slope at the initial price
fprime = 4 * (p - 3)

#the next price is p = p - alpha - fprime
#notice that the slope (fprime) gets smaller and smaller at every iteration, getting closer to 0.
# we can check whether the slope is small enough to break the while loop.

while abs(fprime) > 0.0001:
    fprime = 4 * (p - 3)
    p = p - alpha * fprime
    print(f'updated price: {p}, and slope: {fprime}')

#exercise: finding 3^(1/5)
# x^5 = 3
# f(x) = (x^5 - 3)^2
f'(x) = 2(x^5 - 3)(5x^4)
alpha = 0.000000001
# #start with a random guess for the price
x = 1.5 #find the slope at the initial price
fprime = 2 * ((x ** 5) - 3) * (5 * (x ** 4))
#
# #the next price is p = p - alpha - fprime
# #notice that the slope (fprime) gets smaller and smaller at every iteration, getting closer to 0.
# # we can check whether the slope is small enough to break the while loop.
#
while abs(fprime) > 0.0001:
    fprime = 2 * ((x ** 5) - 3) * (5 * (x ** 4))
    p = p - alpha * fprime
    print(f'updated price: {p}, and slope: {fprime}')

#lists
ages = [34,25,15,76,68,50,23]
# #      -7  -6 -5 -4 -3 -2 -1
# #read the age at index 0
print(ages[0])
print(ages[2])

print(ages[-1])
print(ages[-4])
#
# #slicing lists
# # in the slice a:b, index a is always included while b is excluded
print(ages[1:5]) #prints 1-4, excluding 5
print(ages[-4:-1])

print(ages[2:]) #prints all #s from index 2 to the end of the list
print(ages[:5]) #prints every item before and excluding index 5

k = 2
while k < 6:
    print(ages[k])
    k += 1

#exercise: find the average age
ages = [34,25,15,76,68,50,23]
k = 0
tot = 0
while k < len(ages):
    tot += ages[k]
    k += 1
print(tot)

average = tot/len(ages)
print(average)
average = sum(ages) / len(ages)
print(average)

#exercise: find the number of people older than 49
ages = [34,25,15,76,68,50,23]
old = []
for age in ages:
    if age > 49:
        old.append(age)
print(f'{len(old)} people are over 49 years old.')

#exercise: generalize above function
def count_people_older_than(ages, age_limit):
    counter = []
    for age in ages:
        if age > age_limit:
            counter.append(age)
    print(f'{len(counter)} people are older than {age_limit}.')

ages = [34,25,15,76,68,50,23]
count_people_older_than(ages,51)
