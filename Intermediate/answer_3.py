#Write a Python program to find the intersection of two lists

def findIntersection(list1, list2):

    return list(set(list1) & set(list2))


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("The intersection of the two lists is:", findIntersection(list1, list2))