# Write a Python program to find the common characters between two strings.

def findCommonCharacters(str1, str2):
    return list(set(str1) & set(str2))
    # set1 = set(str1)
    # set2 = set(str2)

    # return sorted(set1.intersection(set2))

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

commonChars = findCommonCharacters(str1, str2)

if commonChars:
    print("Common characters:", ''.join(commonChars), commonChars)
else:
    print("No common characters found.")