#if statement
#example: a store provides a discount when a certain amount threshold is met or exceeded.
#Reduce total price by 10% if 100 dollars or more are spent.

price = float(input('Please enter the total price:'))
# # ^^converting the input to float instead of int stops python from throwing away cents(decimals).

if price >= 100:
    price = 0.9 * price
    print(f' You pay: {price}')
else:
    print(f'You pay: {price}')

#example of if-else
#In a restaurant, a manager makes 50 dollars an hour and a cook makes 35 dollars an hour.
position = input('Enter your position (manager/cook):')
n_hours = float(input('Enter number of hours:'))
salary = None
if position == 'manager':
    salary = 50 * n_hours
elif position == 'cook':
    salary = 35 * n_hours
else:
    print('Error: Invalid input')

print(f'You will earn ${salary}')

#exercise - student grades and letter averages
grade = float(input('Enter your numerical grade:'))
letter = None
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade < 70:
    letter = 'F'

print(f'Your letter grade is {letter}.')

#decision tree function
hunger = input('Are you hungry? (yes/no):')
print(hunger)
if hunger == 'no':
    print('Drink water')
elif hunger == 'yes':
    fruit = input('Is there fruit? (yes/no):')
    print(fruit)
    if fruit == 'yes':
        print('Eat fruit')
    elif fruit == 'no':
        print('Eat a savory snack')

#earthquake magnitude classification function
mag = float(input("Enter earthquake magnitude:"))
print(mag)
if mag < 2.0:
    print('Classification: Micro')
elif mag <= 3.9:
    print('Classification: Minor')
elif mag <= 4.9:
    print('Classification: Light')
elif mag <= 5.9:
    print('Classification: Moderate')
elif mag <= 6.9:
    print('Classification: Strong')
elif mag <= 7.9:
    print('Classification: Major')
elif mag >= 8.0:
    print('Classification: Great')

#improved below

mag = float(input("Enter earthquake magnitude:"))
print(mag)
if mag < 2.0:
    print('Classification: Micro')
elif mag < 4.0:
    print('Classification: Minor')
elif mag < 5.0:
    print('Classification: Light')
elif mag < 6.0:
    print('Classification: Moderate')
elif mag < 7.0:
    print('Classification: Strong')
elif mag < 8.0:
    print('Classification: Major')
elif mag >= 8.0:
    print('Classification: Great')