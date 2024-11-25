#Write a Python program to find the highest occurring character in a string.

from collections import Counter

def highestOccurringCharacter(string):
    char_count = Counter(string)
    max_char = max(char_count, key=char_count.get)
    
    return max_char, char_count[max_char]

input_string = input("Enter a string: ")

if input_string.strip():
    
    char, charCount = highestOccurringCharacter(input_string)
    print(f"The highest occurring character is '{char}' with {charCount} occurrences.")
else:
    print("The input string is empty.")