#create a program that returns the first 10 numbers of the Fibonacci sequence
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


# Get the first 10 Fibonacci numbers
first_10_fib = fibonacci(10)
print(first_10_fib)



