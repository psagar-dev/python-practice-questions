# Write a Python program to find the sum of all elements in a list

def sumOfElements(lst):
    return sum(lst)

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 7,11, 15, 11 ,15 ,7, 5, 6]

result = sumOfElements(input_list)

print(f"The sum of all elements in the list is: {result}")