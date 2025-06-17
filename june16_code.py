def largest(a,b):
    """
    Largest number from given two numbers
    :param a: first number
    :param b: second number
    :return: returns a if a > b, otherwise returns b.
    """
    if a > b:
        return a
    else:
        return b

# print(largest(5,9))

def largest_three(a,b,c):
    """
    Largest number from given three numbers
    :param a: first number
    :param b: second number
    :param c: third number
    :return: largest number
    """
    if a >= b and a >= c: #using >= prevents equal numbers from creating a bug
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# print(largest_three(200,200,5))

#the above approach would not be practical for comparing lots of numbers.
def largest_n(a,b,c):
    # a separate variable to keep track of the maximum
    lv = 0
    if a >= lv:
        lv = a
    if b >= lv:
        lv = b
    if c >= lv:
        lv = c

    return lv

# print(largest_n(-20,-5,-30))

#however, the above will not work for negative numbers as the initialized largest number, 0, will be greater than them.
# to fix this problem, we need to make sure that lv is as small as possible.
def largest_n_2(a,b,c):
    # a separate variable to keep track of the maximum
    lv = float("-inf")
    if a >= lv:
        lv = a
    if b >= lv:
        lv = b
    if c >= lv:
        lv = c

    return lv

# print(largest_n_2(-20,-5,-30))

#we can reduce the number of comparisons by randomly assigning one of the variables as the largest value.
def largest_n_3(a,b,c):
    # a separate variable to keep track of the maximum
    lv = a
    if b >= lv:
        lv = b
    if c >= lv:
        lv = c

    return lv

# print(largest_n_3(-20,-5,-30))
#the above approach is much faster than the very first, but it receives variables separately. It might be easier to
#place all the numbers in a list and provide it to the function.
def my_maximum(v):
    """
    finds maximum
    :param v: list of numbers to find a maximum from
    :return: the largest number
    """
    large = v[0]
    for i in v:
        if i > large:
            large = i

    return large

v = [-2,5,0,7,10,-1,8]
# print(my_maximum(v))

def my_minimum(v):
    small = v[0]
    k = 1
    for i in v:
        if i < small:
            small = i

    return small

# print(my_minimum(v))

#Dictionaries
# we can create a dictionary using this syntax:
# english = {word1 : meaning1, word2 : meaning2, ..., wordN : meaningN}
#each item is a pair of a key and value
english = {'hello' : 'a common greeting', 'goodbye' : 'said right before leaving'}

#we can reach each item by using its key in subscript notation
# print(english['hello'])

#we can add more items to the dictionary
english['morning'] = 'the time when the sun rises'
# print(english)

#we can check if a key exists in a given dictionary
def is_key_a(A):
    if 'car' in A:
        print(A['car']) #this will be true if 'car' exists in A
    else:
        print(f'car is not a key')

A = {'dog': 2, 'cat':5}
# print(is_key_a(A))

#Exercise
#write a function accepting a list of strings, either 'dog' or 'cat', that returns a dictionary with the counts
#of these animals.
animals = ['dog', 'cat', 'dog', 'cat', 'cat', 'cat', 'dog']

def animal_count(string): #my solution
    dogs = string.count('dog')
    cats = string.count('cat')
    result_dict = {'dog': dogs, 'cat': cats}

    return result_dict

# print(animal_count(animals))

def animal_counter(v): #provided solution
    res = {}
    for animal in v:
        if animal not in res:
            res[animal] = 1
            continue
        res[animal] += 1

    return res

# print(animal_counter(animals))

#let us define a function that receives a list v and returns a list of unique values. use only lists, no dictionaries.
def unique_vals(v):
    res = []
    for i in v:
        if i not in res:
            res.append(i)

    return res

v = [1,2,2,3,3,4,4,5,6,8,8,8,10,56]
# print(unique_vals(v))

animals = ['dog', 'cat', 'dog', 'cat', 'cat', 'cat', 'dog', 'rabbit']
# print(unique_vals(animals))

#lets do this but with dictionaries
def animal_counter_dict(v):
    res = {}
    for item in v:
        res[item] = 0
    for animal in v:
        res[animal] += 1

    return res

# print(animal_counter_dict(animals))

def winner(d):
    key_ = None
    value_ = float("-inf")
    winner_key = max(d, key=d.get)
    winner_value = d[winner_key]
    for (key, value) in d.items():
        if value > value_:
            value_ = value
            key_ = key

    return key_, value_

animals = ['dog', 'cat', 'dog', 'cat', 'cat', 'cat', 'dog']
animal_counts = animal_counter(animals)
print(animal_counts)
largest_count = winner(animal_counts)
print(largest_count)

#KNN (K-nearest neighbors)

#weights for high school and middle school students
W_pos = [50,60,70,65]
W_neg = [40,55,52,41,43]
#weight of a test person
T = 45

#Use 1NN to classify T into pos (high school) or neg (middle school)
#1. find the nearest weight in W_pos to T
#2. find the nearest weight in W_neg to T
#3. find the smallest difference of the two and choose its pos

def smallest_distance(T, v):
    """
    finds the distance to the nearest element of v to T.
    :param T: the test point (scalar)
    :param v: the list of numbers (list)
    :return: the smallest distance from T to the nearest element in v
    """
    distances = []
    for i in v:
        distances.append(abs(T-i))
    smallest = min(distances)
    return smallest

d_pos = smallest_distance(T, W_pos)
d_neg = smallest_distance(T, W_neg)

print(d_pos, d_neg)

if d_pos < d_neg:
    print('Positive class')
else:
    print('Negative class')