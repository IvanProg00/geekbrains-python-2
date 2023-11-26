def read_list_numbers(mess):
    data = input(mess)
    return [int(num) for num in data.split(" ")]


def count_pairs(nums):
    count = 0

    for n in set(nums):
        count += nums.count(n) // 2

    return count


nums = read_list_numbers("Enter the list of numbers: ")

res = count_pairs(nums)

print(res)
