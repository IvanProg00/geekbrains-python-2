max_value = int(input("Enter the maximum number: "))

num = 0

while True:
    val = 2 ** num

    if val > max_value:
        break

    print(f"2^{num} = {val}")
    num += 1
