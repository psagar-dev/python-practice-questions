# Write a Python program to find the average of a list of numbers.

def calculateAverage(numbers):
    lenNumber = len(numbers)
    if lenNumber == 0:
        return 0
    
    return int(sum(numbers) / lenNumber)


input_numbers = [10, 20, 30, 40, 50, 60]

print(f"The average is: {calculateAverage(input_numbers)}")
