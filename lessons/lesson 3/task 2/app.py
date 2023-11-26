arr = [0, -1, 5, 2, 3]

# count = 0

# for i in range(1, len(arr)):
#     if arr[i] > arr[i-1]:
#         count += 1

count = len([arr[i] for i in range(1, len(arr)) if arr[i] > arr[i-1]])

print(count)
