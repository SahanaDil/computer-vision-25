# #print numbers from 1 to 10
#
# #solution 1
for i in range (1, 11):
    print(i)
#
# #solution 2
counter = 0
while counter < 10:
    counter += 1
    print(counter)
#
# #solution 3
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

#solution 4
counter = 1
while counter < 11:
    print(counter)
    counter += 1

# #exercise
# #write a program with a while loop that prints numbers with intervals of 5 from 1 to 100.
k = 0
while k < 101:
    print(k)
    k += 5

#summing numbers 1 to 10 (pecans)
total = 0
inc = 1
while inc < 11:
    total += inc
    inc += 1
print(total)

# # exercise
# 1 + 4 + 7 + 10 + .. + 301
k = 1
tot = 0
while k <= 301:
    tot += k
    k += 3
print(tot)

# #check if a number is a multiple of 5
def is_multiple_of_five(n):
    if n % 5 == 0:
        return True
    else:
        return False

# is_multiple_of_five(1051)

# #solution 1
k = 0
while k <= 100:
    if is_multiple_of_five(k) is True:
        print(k)
    k += 1

# #solution 2
k = 0
while k <= 100:
    D = is_multiple_of_five(k)
    if D:
        print(f'{k} is divisible by 5')
    k += 1

#exercise: multiples of 13 finder
def is_mult_thirteen(n):
    if n % 13 == 0:
        return True
    else:
        return False

m = 0
while m <= 100:
    if is_mult_thirteen(m) is True:
        print(m)
    m += 1

# writing a multiple finder for every number is redundant. we can generalize this into one function.
def is_mult_number(n, k):
    if n % k == 0:
        print(True)
        return True

    else:
        print(False)
        return False

# is_mult_number(500,50)

#exercise: write a program that prints all the integers divisible by 5 between integers A and B.
def multiple_of_five(a, b):
    while a % 5 != 0:
        a += 1
    print(a)
    while b % 5 != 0:
        b -= 1
    while a < b:
        a += 5
        print(a)

# multiple_of_five(47,103)

#better version
def multiples_of_five(m, n):
    while is_multiple_of_five(m) is False:
        m += 1
    while m < n:
        print(m)
        m += 5

# multiples_of_five(47,103)

#exercise - prime number checker
def is_prime(n):
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

# is_prime(2)

#exercise - finding prime numbers up to a given number, n
def prime_numbers_upto(n):
    for i in range (2,n+1):
        if is_prime(i) is True:
            print(i)

# prime_numbers_upto(100)

#simple perceptron
def perceptron(a1,a2,w0,w1,w2):
    #find the net sum ynet
    ynet = (1 * w0) + (a1 * w1) + (a2 * w2)
    print('ynet:', ynet)
    #check if ynet is positive or negative
    if ynet >= 0:
        print('positive class')
    elif ynet < 0:
        print('negative class')

perceptron(10,5,1,-3,2)
