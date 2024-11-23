# Write a Python program to find the Fibonacci series up to a given number of terms

def fibonacciSeries(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence

number_input = int(input("Enter the number of terms for the Fibonacci series: "))

print(fibonacciSeries(number_input))