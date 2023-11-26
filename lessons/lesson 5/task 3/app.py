def is_primer_number(n: int) -> bool:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


num = int(input("Enter the number: "))

if is_primer_number(num):
    print("the number is primer")
else:
    print("the number is not primer")
