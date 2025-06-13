print('Hello Houston')
print(4+5)
print(8-20)
print(5+10-3+7)
print(9*5)
print(10/5 * 3)
print(10/(5 * 3))
print(10 + 2 * 5 - 50 / 25)

#we are finding the circumference of a rectangle with W = 5 and L = 7
# if you forget to use parentheses, the result would be wrong
print(2*(7+5))

# The modulus operation is a % b. it finds the remainder of the division a/b.
print(27 % 5) #result 2
print(87993423 % 10) #result 3

#exponentiation operator. a ** b finds the result of a raised to the power of b.
print(5 ** 3) #result 125
print(13 ** 50)

#compute the area of a circle with radius of 10
print(3.14 * (10 ** 2))
#the above was a rough estimation of pi, let us use a more precise approximation
print(3.1415926535897932 * (10 ** 2))

#Area of a circle with radius 17
print(3.1415926535897932 * 17 * 17)

#let us assign a variable to the long number, pi
pi = 3.1415926535897932
print(pi * 10 * 10)
print(pi * 17 * 17)

#we can also use the name 'r' to represent radius values
r = 10
print(pi * r * r)

#Exercise
#Compute the volume of a cylinder with r = 10 and h = 7
h = 7
print( pi * (r ** 2 ) * h) #result 2199.11485...

#volume of 3 different cylinders
r1 = 10
h1 = 12
print("Volume of cylinder 1:", (pi * (r1 ** 2 ) * h1))

r2 = 5
h2 = 7
print("Volume of cylinder 2:", (pi * (r2 ** 2 ) * h2))

r3 = 7
h3 = 10
print("Volume of cylinder 3:", (pi * (r3 ** 2 ) * h3))

#area of three different circles
rA = 5
rB = 10
rC = 7

print("Area of circle A:", (pi * (rA **2 )))
print("Area of circle B:", (pi * (rB **2 )))
print("Area of circle C:", (pi * (rC **2 )))

#we can be more descriptive
print("Area of circle A with radius 5:", (pi * (rA ** 2)))
print("Area of circle B with radius 10:", (pi * (rB ** 2)))
print("Area of circle C with radius 7:", (pi * (rC ** 2)))

#hardcoding strings is prone to error. to avoid this, we can use f strings.
print(f'Area of circle A with radius {rA}:', (pi * (rA ** 2)))
print(f'Area of circle B with radius {rB}:', (pi * (rB ** 2)))
print(f'Area of circle C with radius {rC}:', (pi * (rC ** 2)))

#Instead of using two arguments in the above print statements, we can use a single f-string
print(f'Area of circle with radius {rA}: {pi * (rA ** 2)}')
print(f'Area of circle with radius {rB}: {pi * (rB ** 2)}')
print(f'Area of circle with radius {rC}: {pi * (rC ** 2)}')

#the above print lines are redundant, we can use a function instead
def circle_area(r):
    print(f'Area of the circle with r = {r} is {pi * (r ** 2)}')


circle_area(5)
circle_area(10)
circle_area(7)

def sum_upto(N):
    print(f'1 + 2 + ... + {N} = {N * (N+1)/2}')


sum_upto(100)
sum_upto(255)

def cylinder_volume(r, h):
    print(f'The volume of a cylinder with radius {r} and height {h} is {pi * (r ** 2) * h}.')


cylinder_volume(5,10)
cylinder_volume(10,12)
