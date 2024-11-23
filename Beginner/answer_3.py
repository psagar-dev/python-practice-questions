# Write a Python program to check if a number is prime.
def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():

    userInput  = int(input("Enter a number: ").strip())

    if isPrime(userInput):
        print(f"{userInput} is a prime number.")
    else:
        print(f"{userInput} is not a prime number.")


main()