# Write a Python program to check if a number is even or odd

def is_even_or_odd(number):
     
    if number % 2 == 0:
        return f"The number {number} is even"
    else:
        return f"The number {number} is odd"


def main():
    try:

        user_input = input("Enter a number: ").strip()
        number = int(user_input)

        result = is_even_or_odd(number)
        print(result)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()