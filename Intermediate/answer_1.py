#Write a Python program to find the second largest number in a list.

def findSecondLargest(numbers):
    unique_nums = sorted(set(numbers), reverse=True)
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]

input_numbers = [10, 20, 4, 45, 99, 20]

second_largest = findSecondLargest(input_numbers)

if second_largest is not None:
    print(f"The second largest number is: {second_largest}")
else:
    print("The list does not have a second largest number.")