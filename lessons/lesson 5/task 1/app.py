def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter n the fibonacci number: "))
fib_num = fibonacci(num)

print(f"the fibonacci number is {fib_num}")
