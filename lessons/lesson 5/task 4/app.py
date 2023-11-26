def print_reverse_numbers(count_nums: int):
    user_num = int(input("Enter the number: "))
    if count_nums > 1:
        print_reverse_numbers(count_nums - 1)
    else:
        print("____________________")
    print(user_num, end=" ")


count_nums = int(input("Enter the count of numbers: "))
print_reverse_numbers(count_nums)
