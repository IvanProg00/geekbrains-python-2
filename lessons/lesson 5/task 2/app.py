def replace_max_and_min(arr: list[int]):
    min_num = min(arr)
    max_num = max(arr)

    for i in range(len(arr)):
        if arr[i] == max_num:
            arr[i] = min_num


grades = [1, 2, 3, 1, 2, 1, 5, 4, 5]

print(f"before: {grades}")
replace_max_and_min(grades)
print(f"after: {grades}")
