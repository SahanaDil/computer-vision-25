#question 1 (printing multiples of 3 and 7 upto 100)
k = 0
while k < 100:
    k += 1
    if k % 3 != 0 and k % 7 != 0:
        continue
    else:
        print(k)


#question 2(finds multiplicative factors of a given integer n)
def find_factors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i)

find_factors(24)

#question 3 (finds prime factors of a given integer N)
def prime_factors(n):
    factors = []
    k = 2
    while n > 1:
        if n % k == 0:
            factors.append(k)
            n = n // k
        else:
            k += 1
    print(factors)
    # if you multiply the prime factors printed, you will get the number n

# prime_factors(24)

#question 4 (counting number of subzero days in a given list of temperatures)
def count_subzero_days(temperatures):
    count = 0
    for temp in temperatures:
        if temp < 0:
            count += 1
    print(f'{count} days have subzero temperatures.')


temps = [5, -2, 0, 3, -7, 8, -1, 4, -5, 6, 2, -3, 7, -4, 1]
count_subzero_days(temps)
