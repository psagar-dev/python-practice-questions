# Write a Python program to find the square root of a number.

import math

number_input = float(input('Enter a number to find its square root: '))

if number_input >= 0:
    print(f"The square root of {number_input} is {math.sqrt(number_input)}")
else:
    print("Square root of negative numbers is not a real number.")