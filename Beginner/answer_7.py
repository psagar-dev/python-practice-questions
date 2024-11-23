# Write a Python program to count the number of vowels in a string.

def countVowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
            
    return count


input_string =  input("Enter a string: ")

print(f"Number of vowels: {countVowels(input_string)}")