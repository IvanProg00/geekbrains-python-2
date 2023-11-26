arr = [1, 2, 3, 4, 5, 6, 7]
move = 3

# for _ in range(move):
#     arr.insert(0, arr.pop())

arr = arr[-move:] + arr[:-move]

print(arr)
