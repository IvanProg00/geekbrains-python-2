nums = [int(num) for num in input("Enter the list of numbers: ").split(" ")]
min_num = int(input("Enter the minimum number: "))
max_num = int(input("Enter the maximum number: "))

res = [i for i in range(len(nums)) if nums[i] >= min_num and nums[i] <= max_num]

print(res)
