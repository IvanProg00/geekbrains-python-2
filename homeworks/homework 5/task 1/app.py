def power(num: int, grade: int) -> int:
    if grade == 0:
        return 1

    return num * power(num, grade - 1)


num = int(input("Enter the number: "))
grade = int(input("Enter the power: "))

res = power(num, grade)
print(f"{num}^{grade} = {res}")
