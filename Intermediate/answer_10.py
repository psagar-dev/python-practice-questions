#Write a Python program to find the first non-repeating character in a string.

from collections import Counter

def firstNonRepeatingChar(s):
    char_count = Counter(s)
    
    for char, key in char_count.items():
        if(key == 1):
            return char
        
input_string = input("Enter a string: ")
print(f"The first non-repeating character is: {firstNonRepeatingChar(input_string)}")
