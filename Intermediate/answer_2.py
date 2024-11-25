#Write a Python program to count the frequency of each element in a list.

from collections import Counter

def countFrequency(elements):
    return Counter(elements)

input_number = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,4,6,6]

frequencies  = countFrequency(input_number)

for element, frequency in frequencies.items():
    print(f"{element}:{frequency}")