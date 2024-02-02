def fibonacci(n):
    if n < 2:
        return n

    fib_minus_one = 1
    fib_minus_two = 0
    fib = 0

    for index in range(2, n + 1):
        fib = fib_minus_one + fib_minus_two
        fib_minus_two = fib_minus_one
        fib_minus_one = fib

    return fib

