#Write a Python program to count the occurrences of each element in a list.

from collections import Counter

def countOccurrences(lst):
    return dict(Counter(lst))


example_list = [1, 2, 2, 3, 3, 4,4,4,4,4,4, 5,5, 5]

print(countOccurrences(example_list))