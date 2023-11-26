first_num = int(input("Enter the first number of array: "))
diff = int(input("Enter the difference: "))
size = int(input("Enter the number of elements: "))

res = []

for i in range(size):
    res.append(first_num + i * diff)

print(res)
