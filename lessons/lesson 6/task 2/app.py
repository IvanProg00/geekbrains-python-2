def read_list_numbers(mess):
    data = input(mess)
    return [int(num) for num in data.split(" ")]


def count_lower_neighbor(nums):
    count = 0

    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            count += 1

    return count


nums = read_list_numbers("Enter the list of numbers: ")

res = count_lower_neighbor(nums)

print(res)
