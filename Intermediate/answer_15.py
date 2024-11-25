#Write a Python program to find the missing number in a given list of consecutive numbers

def findMissingNumber(numbers):

    n = len(numbers) + 1
    
    expected_sum = n * (numbers[0] + numbers[-1]) // 2
    actual_sum = sum(numbers)
    
    return expected_sum - actual_sum

input_number = [1, 2, 3, 5, 6]

print(f"The missing number is: {findMissingNumber(input_number)}")