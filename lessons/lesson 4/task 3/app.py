# Ваня
n = int(input())
# Если число положительное и пользователь вводит число меньше, то никогда не будет
# число пользователя максимальным
max_number = 1000
while n != 0:
    n = int(input())
    if max_number > n:  # Мы должны менять max_number, если max_number < n
        max_number = n
print("Ваня", max_number)

# Петя:
n = int(input())
max_number = -1
while n < 0:  # Цикл должен рабатать пока числа положительные
    n = int(input())
    if max_number < n:
        n = max_number  # Должно быть наоборот
print("Петя", n)  # Должна быть max_number


# Должно быть
n = int(input())
max_number = -1
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)
