# Write a Python program to find the sum of all prime numbers in a given range.

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sumOfPrimes(start, end):
    return sum(num for num in range(start, end + 1) if isPrime(num))

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the start of the range: "))

print(f"The sum of all prime numbers between {start_range} and {end_range} is: {sumOfPrimes(start_range, end_range)}")
