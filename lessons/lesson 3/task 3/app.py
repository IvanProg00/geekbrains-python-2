arr = [1, 1, 2, 0, -1, 3, 4, 4]

res = len(set(arr))
print(res)

# Print the numbers that repeat only once.

# result = []

# for i in set(arr):
#     if arr.count(i) == 1:
#         result.append(i)

result = [i for i in set(arr) if arr.count(i) == 1]

print(result, len(result))
