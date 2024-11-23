# Write a Python program to find the largest and smallest numbers in a list.

def findLargestSmallest(numbers):
    return max(numbers), min(numbers)


input_numbers = [23, 56, 1, 12, 89, 7, 90, 34]

largest, smallest = findLargestSmallest(input_numbers)

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")