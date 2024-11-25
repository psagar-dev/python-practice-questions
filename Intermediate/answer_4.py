#Write a Python program to check if a string is an anagram of another string.

def isAnagram(str1, str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    return sorted(str1) == sorted(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

is_anagram = isAnagram(string1, string2)

if is_anagram:
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')