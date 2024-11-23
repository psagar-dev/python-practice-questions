#Write a Python program to find the sum of all even numbers in a list.

def sumOfEvenNumbers(numbers):
    # First Approach
    # evenSum = []
    # for num in numbers:
    #     if num % 2 == 0:
    #      evenSum.append(num)
    # Second Approach
    return sum(num for num in numbers if num % 2 == 0)
   # return sum(evenSum)

input_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"The sum of all even numbers in the list is: {sumOfEvenNumbers(input_number)}")