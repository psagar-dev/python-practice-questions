# Write a Python program to generate a random number between a given range.

import random

def generateRandomNumber(start, end):
    return random.randint(start, end)
    

start_input = int(input('Enter the starting number: '))
end_input = int(input('Enter the Ending number: '))

print(f"Random number between {start_input} and {end_input}: {generateRandomNumber(start_input, end_input)}")