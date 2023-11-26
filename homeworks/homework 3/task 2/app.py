arr_size = int(input('Enter the number of elements in array: '))
arr = []

for i in range(arr_size):
    num = int(input("Enter the number of array: "))
    arr.append(num)

user_num = int(
    input("Enter the number, to check which number is the closest: "))
closest = arr[0]

for i in range(1, len(arr)):
    if abs(arr[i] - user_num) < abs(closest - user_num):
        closest = arr[i]

print(f'The number {closest} is the closest')
