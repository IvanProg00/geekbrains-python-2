def find_div_sum(num):
    res = 0

    for i in range(1, num // 2 + 1):
        if num % i == 0:
            res += i

    return res


def find_div_sum_pairs(k):
    res = []

    for i in range(k):
        second = find_div_sum(i)
        first = find_div_sum(second)

        if i == first and i != second and (second, i) not in res:
            res.append((i, second))

    return res


k = int(input("Enter the number: "))
res = find_div_sum_pairs(k)

print(res)
