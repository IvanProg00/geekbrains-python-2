def sum_nums(a: int, b: int) -> int:
    if b <= 0:
        return a

    return sum_nums(a + 1, b - 1)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

res = sum_nums(num1, num2)
print(f"{num1} + {num2} = {res}")
