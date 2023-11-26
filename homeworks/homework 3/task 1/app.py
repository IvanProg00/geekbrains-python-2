arr_size = int(input('Enter the number of elements in array: '))
arr = []

for i in range(arr_size):
    num = int(input("Enter the number of array: "))
    arr.append(num)

user_num = int(input("Enter the number, to check how many times it occurs: "))
count = 0


for num in arr:
    if num == user_num:
        count += 1

print(f'The number {user_num} occurs {count} times')