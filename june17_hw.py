import numpy as np

#histogram
N = np.array([[5,2,0,1,5],
              [3,0,1,1,2],
              [0,1,4,2,1]
             ])
#    0,1,2,3,4,5   counts of
h = [3,5,3,1,1,2] # expected answer

def histogram(n):
    length = n.max()
    h = np.zeros(length + 1)
    row, col = n.shape
    for i in range(row):
        for j in range(col):
            val = n[i,j]
            h[val] += 1

    return h

print(histogram(N)) #matches the answer