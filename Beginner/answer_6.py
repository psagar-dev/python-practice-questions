# Write a Python program to find the largest number in a list.
def find_largest_number(numbers):
    return max(numbers)

numbers_list = [10, 24, 99, 32, 98, 3, 77]

largest = find_largest_number(numbers_list)

print(largest)