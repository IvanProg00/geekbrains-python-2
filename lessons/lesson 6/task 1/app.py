def get_unused_values(array_1, array_2):
    res = []

    for num in set(array_1):
        if num not in array_2:
            res.append(num)

    return res


def read_list_numbers(mess):
    data = input(mess)
    return [int(num) for num in data.split(" ")]


# list_1 = [1, 2, 3, 4, 5, 6]
# list_2 = [4, 5, 6, 7, 8]
list_1 = read_list_numbers("Enter the first list of number: ")
list_2 = read_list_numbers("Enter the second list of number: ")

res = get_unused_values(list_1, list_2)

print(res)
