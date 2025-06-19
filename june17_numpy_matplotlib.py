import numpy as np

#create a python list
nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums)

#create a numpy array
v = np.array([1,2,3,4,5,6,7,8,9,10])
# print(v)

#numpy specializes in scientific computation. though we can use python lists and operators, their abilities are limited.
v_new = v + 5

nums_new = []
for num in nums:
    nums_new.append(num+5)
# print(nums_new) #we needed to write a for loop for the same thing numpy accomplished in one line.

#let us look at another example
#assume we have two arrays and we would like to perform elementwise addition
u = np.array([-2,0,5,-4,10])
v = np.array([12,3,-2,4,25])

# print(u + v)

#lets do the same thing with plain python
y = []
for (u_num, v_num) in zip(u,v):
    y.append(u_num + v_num)
# print(y)

#numpy has many functions that we can use.
u = np.array([-2,0,5,-4,10])
# print(u)
u_sum = np.sum(u)
# print(u_sum)

#indexing
# print(u[0])
# print(u[3])
# print(u[-3])

#exercise: write a program that finds the intervals of ones where each interval has at least 2 ones

u = np.array([0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0])
def np_intervals(u):
    u_len = len(u)
    n_regions = 0
    k = 1
    while k < u_len:
        if u[k] == 1 and u[k-1] == 1:
            n_regions += 1
        while u[k] == 1:
            k += 1
            continue

# print(n_regions)

#two dimensional numpy arrays (matrices)
A = np.array([[5,0,-2,3],[0,3,-1,7],[8,0,5,1]])
# print(A)

M = np.array([
    [3, 0, 5, 1, 7, 9, 6, 2, 8, 4],
    [4, 8, 1, 3, 5, 2, 0, 6, 9, 7],
    [9, 7, 2, 0, 6, 1, 4, 3, 5, 8],
    [2, 3, 4, -7, 1, 8, 5, 0, 6, 9],
    [6, 5, 0, 2, 9, 4, 7, 1, 3, 0],
    [1, 9, 3, 6, 0, 7, 8, 4, 2, 5],
    [0, 6, 8, 4, 3, 5, 2, 9, 1, 7],
    [5, 2, 7, 9, 8, 0, 1, 3, 4, 6]
])
# print(M[2:5, 1:3])
print('------')

# print(M[2:5, 4:9]) #second to fourth row excluding five, fourth to eighth column excluding nine
print('------')

# print(M[:, 1:4])
print('------')
# print(M[2:, :3]) #row 3 to last, column 0 to 2

def find_array_negs(M):
    neg = []
    n_rows, n_cols = M.shape
    for i in range(n_rows):
        for j in range(n_cols):
            if M[i, j] < 0:
                neg.append(M[i, j])

    return len(neg)
#exercise: write a program which finds the number of negative numbers in M
# print(find_array_negs(M))

#we can achieve the same result in a single line using numpy
# print((M < 0).sum())

#for explanation
B = np.array([
    [-2,3,0,7,-5],
    [0,-2,8,5,1],
    [9,-4,1,2,6]
])

C = (B < 0)
# print(C) #prints an array of booleans checking each number against the condition
# [[ True False False False  True]
#  [False  True False False False]
#  [False  True False False False]]

C_sum = C.sum()
# print(C_sum)

#exercise: find the sum of all negative numbers in A_a
A_a = np.array([
    [-2,3,0,7,-5],
    [0,-2,8,5,1],
    [9,-4,1,2,6]
])

Aa_neg = A_a[A_a < 0].sum() #this works because of subscript
print(Aa_neg)

Aa_pos = A_a[A_a > 0].sum()
print(Aa_pos)