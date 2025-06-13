#problem 1
def name_of_day(day_number):
    if day_number in [1, 8, 15, 22, 29]:
        print('Monday')
    elif day_number in [2,9,16,23,30]:
        print('Tuesday')
    elif day_number in [3,10,17,24,31]:
        print('Wednesday')
    elif day_number in [4,11,18,25]:
        print('Thursday')
    elif day_number in [5,12,19,26]:
        print('Friday')
    elif day_number in [6,13,20,27]:
        print('Saturday')
    elif day_number in [7,14,21,28]:
        print('Sunday')
    else:
        print('Invalid day number')

name_of_day(27)

#problem 2
k = 7
while k <= 87:
    print(k)
    k += 4

#problem 3
k = 7
tot = 0
while k <= 87:
    tot += k
    k += 4
print(tot)

#problem 4
def fibonacci_numbers_upto(n):
    sequence = []
    a = 1
    b = 1
    while a <= n:
        sequence.append(a)
        a,b = b, a+b
    print(sequence)

fibonacci_numbers_upto(34)

