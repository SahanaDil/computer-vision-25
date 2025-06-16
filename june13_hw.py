# Homework June 13, 2025
# 1. Write a function that takes a list of 0s and 1s as an input
# argument and returns the number of contiguous intervals of 1s in
# that list.

def find_intervals(input):
    count = 0
    if input[0] == 1:
     count += 1
    for i in range(1, len(input)):
        if input[i] == 1 and input[i-1] == 0:
                    count += 1
        elif input[i-1] == 1 and input[i] == 1:
            continue
    print(count)

#running with examples
find_intervals( [0, 1, 1, 0, 1, 1, 1, 0]) #result is 2
find_intervals([0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0] ) #result is 4