set_1_size = int(input("Enter the size of the first array: "))
set_2_size = int(input("Enter the size of the second array: "))

set_1 = set()
for i in range(set_1_size):
    num = int(input("Enter the number for the first array: "))
    set_1.add(num)

set_2 = set()
for i in range(set_2_size):
    num = int(input("Enter the number for the second array: "))
    set_2.add(num)

result_set = set_1.intersection(set_2)

res = list(result_set)
res.sort()

print(f"Result: {res}")
