numbers_sum = int(input("Enter sum of the numbers: "))
numbers_product = int(input("Enter product of the numbers: "))

max_num = min(numbers_sum, numbers_product, 1_000)+1
num_x = 0
num_y = 0

for x in range(1, max_num):
    for y in range(x, max_num):
        if x + y == numbers_sum and x * y == numbers_product:
            num_x = x
            num_y = y

if num_x == 0 and num_y == 0:
    print("The numbers not found")
else:
    print(f"The numbers are {num_x} and {num_y}")
