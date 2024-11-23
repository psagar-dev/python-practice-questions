#Write a Python program to find the common elements between two lists
def findCommonElement(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 2, 7, 8]

common = findCommonElement(list1, list2)

print(f"Common elements: {common}")